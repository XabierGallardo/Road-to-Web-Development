# Ejemplo pequeño con **Angular** (SPA) + API de ejemplo

La app tiene dos rutas: lista de artículos y detalle. Usa `HttpClient` para consumir una API (puedes simularla con `json-server` o una pequeña API Express).

---

## 1) Crear el proyecto Angular (CLI)

```bash
# si no tienes Angular CLI:
npm install -g @angular/cli

# crear proyecto con routing
ng new angular-spa-ejemplo --routing --style=scss
cd angular-spa-ejemplo
```

---

## 2) Generar componentes y servicio

```bash
ng g c pages/articles-list
ng g c pages/article-detail
ng g s services/articles
```

---

## 3) `app-routing.module.ts`

```ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ArticlesListComponent } from './pages/articles-list/articles-list.component';
import { ArticleDetailComponent } from './pages/article-detail/article-detail.component';

const routes: Routes = [
  { path: '', redirectTo: 'articles', pathMatch: 'full' },
  { path: 'articles', component: ArticlesListComponent },
  { path: 'articles/:id', component: ArticleDetailComponent },
  { path: '**', redirectTo: 'articles' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

---

## 4) Servicio `articles.service.ts`

```ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Article {
  id: number;
  title: string;
  body: string;
}

@Injectable({
  providedIn: 'root'
})
export class ArticlesService {
  private api = '/api/articles'; // ajusta al endpoint real

  constructor(private http: HttpClient) {}

  list(): Observable<Article[]> {
    return this.http.get<Article[]>(this.api);
  }

  get(id: number): Observable<Article> {
    return this.http.get<Article>(`${this.api}/${id}`);
  }
}
```

No olvides añadir `HttpClientModule` en `app.module.ts`.

---

## 5) `articles-list.component.ts`

```ts
import { Component, OnInit } from '@angular/core';
import { ArticlesService, Article } from '../../services/articles.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-articles-list',
  templateUrl: './articles-list.component.html',
  styleUrls: ['./articles-list.component.scss']
})
export class ArticlesListComponent implements OnInit {
  articles: Article[] = [];
  loading = true;
  error: string | null = null;

  constructor(private svc: ArticlesService, private router: Router) {}

  ngOnInit(): void {
    this.svc.list().subscribe({
      next: data => { this.articles = data; this.loading = false; },
      error: err => { this.error = err.message || 'Error cargando'; this.loading = false; }
    });
  }

  goDetail(a: Article) {
    this.router.navigate(['/articles', a.id]);
  }
}
```

`articles-list.component.html`:

```html
<div *ngIf="loading">Cargando...</div>
<div *ngIf="error" class="error">{{ error }}</div>

<ul *ngIf="!loading && !error">
  <li *ngFor="let a of articles" (click)="goDetail(a)" class="article-item" role="link" tabindex="0">
    <h3>{{ a.title }}</h3>
    <p>{{ a.body | slice:0:120 }}...</p>
  </li>
</ul>
```

---

## 6) `article-detail.component.ts`

```ts
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ArticlesService, Article } from '../../services/articles.service';

@Component({
  selector: 'app-article-detail',
  templateUrl: './article-detail.component.html',
  styleUrls: ['./article-detail.component.scss']
})
export class ArticleDetailComponent implements OnInit {
  article: Article | null = null;
  loading = true;

  constructor(private route: ActivatedRoute, private svc: ArticlesService) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.svc.get(id).subscribe({
      next: data => { this.article = data; this.loading = false; },
      error: () => { this.loading = false; }
    });
  }
}
```

`article-detail.component.html`:

```html
<div *ngIf="loading">Cargando artículo...</div>
<article *ngIf="article">
  <h1>{{ article.title }}</h1>
  <p>{{ article.body }}</p>
  <a routerLink="/articles">Volver</a>
</article>
```

---

## 7) `app.module.ts` (resumen)

Asegúrate de importar `HttpClientModule` y declarar los componentes:

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ArticlesListComponent } from './pages/articles-list/articles-list.component';
import { ArticleDetailComponent } from './pages/article-detail/article-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    ArticlesListComponent,
    ArticleDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

---

## 8) Simular la API (opciones)

### Opción A: `json-server` (rápido)

Crea `db.json`:

```json
{
  "articles": [
    { "id": 1, "title": "Artículo 1", "body": "Contenido del artículo 1..." },
    { "id": 2, "title": "Artículo 2", "body": "Contenido del artículo 2..." }
  ]
}
```

Instala y corre:

```bash
npm i -g json-server
json-server --watch db.json --port 3000
```

En este caso, cambia en `ArticlesService` `private api = 'http://localhost:3000/articles'`.

### Opción B: API simple con Express (rápido)

```js
// server.js
const express = require('express');
const app = express();
const data = require('./db.json'); // mismo formato que json-server

app.get('/api/articles', (req, res) => res.json(data.articles));
app.get('/api/articles/:id', (req, res) => {
  const a = data.articles.find(x => x.id === Number(req.params.id));
  if (!a) return res.status(404).end();
  res.json(a);
});

app.listen(4000, () => console.log('API en http://localhost:4000'));
```

Luego: `node server.js` y usa `http://localhost:4000/api/articles`.

---

## 9) Ejecutar la app Angular

```bash
ng serve --open
# la app correrá en http://localhost:4200
```

---

## 10) Notas sobre SEO y SSR en Angular

* La SPA de arriba **renderiza en cliente**. Para SEO/TTFB puedes usar **Angular Universal** (SSR).
* Para agregar SSR:

```bash
ng add @nguniversal/express-engine
# esto agrega la infraestructura server-side (Express + bundles server)
# build:
npm run build:ssr
npm run serve:ssr
```

Angular Universal hace render del HTML en el servidor para la primera carga y luego "hidrata" en el cliente.

---

# Checklist para decidir entre **MPA**, **SPA** y **SSR**

---

## Criterios (preguntas clave)

1. **SEO / indexación es crítica?**

   * Sí → preferir MPA o SSR/SSG.
   * No → SPA ok.

2. **Primera carga y TTFB deben ser muy rápidos?**

   * Sí → MPA o SSR/SSG.
   * No (priorizas navegación fluida) → SPA con optimizaciones.

3. **Interactividad compleja (editores, dashboards, tiempo real)?**

   * Sí → SPA (framework como Angular/React/Vue).
   * No → MPA o SPA ligera.

4. **Equipo y mantenibilidad**

   * Equipo grande / features complejas → Framework + SPA o SSR con separación clara frontend/backend.
   * Equipo pequeño / contenido estático → MPA o SSG.

5. **Requisitos de accesibilidad y degradado sin JS**

   * Necesitas funcionar sin JS → MPA o SSR con progressively enhanced frontend.
   * No crítico → SPA.

6. **Control sobre SEO social preview (OpenGraph) y metadata dinámica**

   * Necesario → SSR/SSG (o prerender).
   * No crítico → SPA con meta dinámico (pero bots pueden tener problema).

7. **Carga y coste de infraestructura**

   * Quieres simplicidad y menor coste → MPA/SSG (estáticos, CDN).
   * Aceptas más complejidad infra → SPA + API (podría necesitar más procesos y balanceo).

8. **Necesitas offline / PWA?**

   * Sí → SPA/PWA (service workers), possible with SSR hybrid.
   * No → indiferente.

9. **Seguridad y manejo de tokens**

   * Preferencia por HttpOnly cookies y lógica en servidor → SSR/MPA o API con buen backend.
   * Tokens en localStorage (más riesgo XSS) → SPA (siempre con cuidado).

10. **Tiempo de desarrollo / velocidad de entrega**

    * Rápido y simple → MPA o SSG (blogs, landing pages).
    * Producto complejo → SPA + framework (mejor escalabilidad a largo plazo).

---

## Reglas rápidas de decisión (flujo)

1. Si **SEO** es crítico y la app muestra contenido público indexable → **MPA** (si contenido dinámico bajo) o **SSR/SSG** (si quieres estructura SPA pero con SEO).
2. Si la aplicación es una **herramienta interactiva** (dashboard, editor, SPA tipo app desktop) → **SPA** con framework (Angular/React/Vue).
3. Si quieres **lo mejor de ambos** (SEO + interactividad) → **SSR/SSG + Hydration** (Next.js, Nuxt, Angular Universal, SSG + client-side routing).
4. Si tu prioridad es **velocidad y menor coste** para contenido estático → **SSG** (sitios estáticos, generados en build time) y entregar via CDN.

---

## Matriz resumida (recomendación)

| Criterio principal                        | Recomendación                                        |
| ----------------------------------------- | ---------------------------------------------------- |
| SEO y contenido público                   | **MPA** o **SSR/SSG**                                |
| UX tipo aplicación y mucha interactividad | **SPA (framework)**                                  |
| Mejor TTFB + SEO pero interactividad      | **SSR + Hydration**                                  |
| Sitio marketing / blog / docs             | **SSG** (Netlify, Vercel)                            |
| Equipo grande / código organizado         | **SPA con framework** (o monorepo + micro-frontends) |
| Offline / PWA                             | **SPA** con service workers                          |

---

## Ejemplos concretos

* **Blog personal / documentación** → **SSG** (Hugo, Next.js SSG).
* **E-commerce con SEO importante** → **SSR/SSG híbrido** (product pages SSG, cart + checkout en SPA).
* **Panel de administración / ERP** → **SPA** (React/Angular + API).
* **Página corporativa con pocas interacciones** → **MPA** o **SSG**.

---

## Checklist final (rápido) — marca y decide

* ¿SEO crítico? → Sí → SSR/SSG. No → sigue.
* ¿Interactividad compleja? → Sí → SPA. No → MPA/SSG.
* ¿Necesitas offline/PWA? → Sí → SPA.
* ¿Presupuesto infra limitado? → SSG/CDN o MPA.
* ¿Equipo grande y modularidad? → SPA + patterns (state mgmt, CI/CD).
* ¿Quieres lo “mejor” de ambos? → SSR (Angular Universal / Next.js) + Client-side hydration.
