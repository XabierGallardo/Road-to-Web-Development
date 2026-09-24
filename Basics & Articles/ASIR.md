# Administración de Sistemas Informáticos y Redes (ASIR)
**Administración de Sistemas Informáticos y Redes (ASIR)** es un término amplio y paraguas que abarca muchas disciplinas dentro de la infraestructura IT. Tradicionalmente se centraba en:

- **Sistemas operativos** (Windows Server, Linux, etc.)
- **Redes** (configuración, enrutamiento, switching, firewalls)
- **Servicios** (DNS, DHCP, Active Directory, correo, web)
- **Virtualización** y hardware
- **Monitorización** y mantenimiento

Con la evolución de la tecnología, ese paraguas se ha expandido e incluye (o solapa con) áreas como:

- **DevOps** (CI/CD, IaC, contenedores, Kubernetes, automatización)
- **Seguridad informática** (hardening, firewalls, IDS/IPS, gestión de parches, cumplimiento)
- **Cloud computing** (AWS, Azure, GCP)
- **Bases de datos** (administración básica)
- **Scripting/automatización** (Bash, PowerShell, Python)

Dicho esto, conviene matizar:

1. **No son sinónimos exactos.** DevOps y ciberseguridad son disciplinas propias con perfiles especializados. ASIR es la base generalista; DevOps o seguridad son especializaciones o evoluciones de esa base.
2. **En el ámbito académico español**, ASIR es un ciclo formativo de grado superior (Técnico Superior en Administración de Sistemas Informáticos en Red) que da fundamentos de todo esto, pero no te convierte en experto en DevOps ni en seguridad sin formación adicional.
3. **En el mundo laboral**, un administrador de sistemas puede derivar hacia:
   - SysAdmin / Network Admin (lo clásico)
   - DevOps / SRE
   - Seguridad (SOC, pentesting, blue team)
   - Cloud/Infraestructura

**ASIR es el tronco común; DevOps, seguridad, cloud, etc., son ramas que crecen de ese tronco.**



---



## 1. DevOps

### ¿Qué es realmente?

DevOps **no es una herramienta ni un puesto de trabajo concreto**, es una **cultura y un conjunto de prácticas** que busca eliminar la barrera entre Desarrollo (Dev) y Operaciones (Ops). El objetivo es entregar software de forma más rápida, frecuente y fiable.

Nace del problema clásico: los desarrolladores escribían código y "lo lanzaban por encima del muro" a los de sistemas, que tenían que hacerlo funcionar en producción. Cuando algo fallaba, nadie se responsabilizaba. DevOps rompe ese muro con responsabilidad compartida.

### Pilares fundamentales (CALMS)

- **C**ulture: colaboración, feedback, responsabilidad compartida
- **A**utomation: todo lo repetible se automatiza
- **L**ean: eliminar desperdicio, mejorar flujo
- **M**easurement: métricas, observabilidad
- **S**haring: conocimiento compartido, blameless postmortems

### Prácticas clave

| Práctica | Qué implica |
|---|---|
| **CI (Integración Continua)** | Cada commit se integra y testea automáticamente |
| **CD (Entrega/Despliegue Continuo)** | El código llega a producción de forma automatizada |
| **IaC (Infraestructura como Código)** | Terraform, Ansible, Pulumi, CloudFormation |
| **Contenedores** | Docker, Podman |
| **Orquestación** | Kubernetes, Docker Swarm, Nomad |
| **Observabilidad** | Prometheus, Grafana, ELK, OpenTelemetry |
| **GitOps** | ArgoCD, Flux — el repo Git es la fuente de verdad |

### Herramientas típicas

- **CI/CD**: Jenkins, GitLab CI, GitHub Actions, CircleCI, ArgoCD
- **IaC**: Terraform, Ansible, Pulumi
- **Contenedores**: Docker, Kubernetes, Helm
- **Config management**: Ansible, Puppet, Chef
- **Secretos**: Vault, SOPS, Sealed Secrets

### El "problema" de DevOps

Como es una cultura, muchas empresas crearon el rol de **"DevOps Engineer"**, que en la práctica suele ser un **SysAdmin que también automatiza y programa**. Esto ha generado cierta confusión: hay quien dice que "DevOps Engineer" es un antipatrón, porque DevOps debería ser una responsabilidad de todos, no un silo nuevo.

---

## 2. SRE (Site Reliability Engineering)

### ¿Qué es?

SRE nace en **Google** (publicaron el famoso libro en 2016). Es la **implementación concreta de DevOps con principios de ingeniería**. La frase clásica:

> "SRE es lo que pasa cuando le pides a un ingeniero de software que diseñe un equipo de operaciones."

### Diferencia clave con DevOps

| DevOps | SRE |
|---|---|
| Cultura/filosofía | Rol/implementación concreta |
| "¿Cómo hacemos esto?" | "Aquí está la receta concreta" |
| Más amplio y difuso | Más medible y prescriptivo |

En la práctica, SRE es **DevOps con SLA/SLO y presupuesto de error**.

### Conceptos fundamentales

**SLI, SLO, SLA**
- **SLI (Service Level Indicator)**: la métrica real (ej. latencia p95, tasa de error)
- **SLO (Service Level Objective)**: el objetivo interno (ej. 99.9% de disponibilidad)
- **SLA (Service Level Agreement)**: el contrato con el cliente, con consecuencias legales/económicas

**Error Budget (presupuesto de error)**
Si tu SLO es 99.9%, tienes un 0.1% de "presupuesto" para fallar al mes (~43 min). Si lo agotas, se **congelan los despliegues** y el equipo se centra en fiabilidad. Esto alinea a Dev y Ops: nadie quiere quemar el presupuesto.

**Toil**
Trabajo manual, repetitivo, automatizable y sin valor a largo plazo. SRE busca mantenerlo por debajo del 50% del tiempo del equipo.

**Postmortems blameless**
Cuando hay un incidente, se analiza el sistema, no se busca culpables. Se documenta y se generan acciones preventivas.

**Ingeniería del caos**
Chaos Monkey, inyección de fallos controlados para validar resiliencia.

### Perfil del SRE

Suele ser alguien con **base fuerte de sistemas + programación**. Escribe código para automatizar, diseña sistemas distribuidos, entiende redes, Linux, Kubernetes, y sabe de observabilidad y capacidad.

### Herramientas

Prometheus, Grafana, Thanos, Loki, Kubernetes, Terraform, Go/Python, PagerDuty, incident.io.

---

## 3. Cloud / Infraestructura

### ¿Qué es?

Es la rama que se ocupa de **diseñar, desplegar y operar la infraestructura** sobre la que corren las aplicaciones, ya sea on-premise, en cloud público, híbrida o multi-cloud.

### Modelos de servicio cloud

| Modelo | Tú gestionas | El proveedor gestiona | Ejemplo |
|---|---|---|---|
| **IaaS** | SO, runtime, app, datos | Virtualización, red, hardware | EC2, VM Azure |
| **PaaS** | App, datos | Todo lo demás | App Engine, Heroku |
| **SaaS** | Nada (solo uso) | Todo | Gmail, Salesforce |
| **FaaS/Serverless** | Solo funciones | Todo | Lambda, Cloud Functions |
| **CaaS** | Contenedores | Orquestación base | EKS, GKE, AKS |

### Roles dentro de Cloud/Infra

- **Cloud Engineer / Cloud Architect**: diseña la arquitectura cloud
- **Platform Engineer**: construye plataformas internas para devs (IDP)
- **Infrastructure Engineer**: on-prem, redes, virtualización
- **Network Engineer**: redes cloud y on-prem, SDN
- **Cloud Security Engineer**: seguridad específica de cloud

### Áreas de conocimiento

**Fundamentos**
- Redes (VPC, subnets, routing, DNS, load balancers, CDN)
- Cómputo (VMs, contenedores, serverless)
- Almacenamiento (blob, block, file, object storage)
- IAM (identidades, roles, políticas)

**Avanzado**
- **Alta disponibilidad y DR**: multi-AZ, multi-región, RTO/RPO
- **Escalado**: auto-scaling, horizontal vs vertical
- **Costes (FinOps)**: optimización, reserved instances, spot
- **IaC**: Terraform, CDK, Bicep, Pulumi
- **Seguridad**: cifrado, KMS, secrets, zero trust
- **Observabilidad**: logs, métricas, trazas

**Multi-cloud / Híbrido**
- Evitar vendor lock-in
- Consistencia de red y seguridad
- Herramientas: Kubernetes, Terraform, Anthos, Azure Arc

### Proveedores principales

- **AWS**: el más maduro, mayor cuota
- **Azure**: fuerte en empresas y ecosistema Microsoft
- **GCP**: fuerte en datos, Kubernetes (creadores), IA
- **Otros**: Oracle Cloud, IBM Cloud, Alibaba Cloud

### Certificaciones relevantes

- AWS: Solutions Architect, DevOps Engineer
- Azure: AZ-104, AZ-305, AZ-400
- GCP: Associate Cloud Engineer, Professional Cloud Architect
- Kubernetes: CKA, CKAD, CKS

---

## 4. Cómo se relacionan las tres ramas

```
                 ┌─────────────────────┐
                 │   Cloud/Infra       │  ← el "dónde" y el "con qué"
                 │  (AWS, K8s, redes)  │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │      DevOps         │  ← la cultura y prácticas
                 │  (CI/CD, IaC, GitOps)│
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │       SRE           │  ← la ingeniería de fiabilidad
                 │ (SLOs, error budget)│
                 └─────────────────────┘
```

- **Cloud/Infra** es el **sustrato técnico**: sin saber desplegar en AWS o Kubernetes no hay nada.
- **DevOps** es la **cultura y el flujo**: cómo entregas ese software de forma automatizada.
- **SRE** es la **disciplina de fiabilidad**: cómo garantizas que lo que entregas no se cae.

En la práctica, un profesional moderno suele mezclar las tres: sabe Terraform + Kubernetes (Cloud/Infra), monta pipelines CI/CD (DevOps), y define SLOs y alertas (SRE).

---

## 5. Ruta de aprendizaje sugerida

1. **Base sólida**: Linux, redes, scripting (Bash/Python), Git
2. **Cloud**: un proveedor a fondo (AWS o Azure) + certificación
3. **Contenedores**: Docker → Kubernetes (CKA)
4. **IaC**: Terraform + Ansible
5. **CI/CD**: GitHub Actions o GitLab CI + ArgoCD
6. **Observabilidad**: Prometheus + Grafana
7. **SRE**: leer el libro de Google, practicar SLOs y postmortems
8. **Seguridad**: DevSecOps, hardening, IAM

