# 🧠 Monitoring & Logging Integration — PharmaLink

## 📘 Overview
This setup integrates **Prometheus** and **Grafana** for full-stack monitoring of the **PharmaLink** application, which consists of a **Django backend** and a **React frontend**.  
The goal is to collect, visualize, and analyze **system**, **container**, and **application-level** metrics.

---

## ⚙️ Architecture

| Component | Purpose |
|------------|----------|
| **Prometheus** | Collects metrics from all targets and stores time-series data. |
| **Grafana** | Visualizes metrics and dashboards from Prometheus. |
| **Node Exporter** | Exposes host system metrics (CPU, memory, disk, network). |
| **cAdvisor** | Collects Docker container metrics (CPU, memory, I/O usage). |
| **Django App** | Exposes application-level metrics via `django-prometheus`. |

---

## 🧩 Docker Compose Setup

All services are defined in `docker-compose.yml` under the `monitoring/` directory.

### Services
- **Prometheus** → `localhost:9090`
- **Grafana** → `localhost:3000`
- **Node Exporter** → `localhost:9100`
- **cAdvisor** → `localhost:8080`
- **Django App** → `localhost:8000`

### Start the Stack
```bash
docker-compose up -d
```

### Stop the Stack
```bash
docker-compose down
```

---

## 🧾 Prometheus Configuration

File: `prometheus.yml`

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'django-app'
    static_configs:
      - targets: ['django-app:8000']
```

---

## 📊 Grafana Configuration

1. Open Grafana → [http://localhost:3000](http://localhost:3000)
2. **Login:**  
   - Username: `admin`  
   - Password: `admin` (change when prompted)
3. Add **Prometheus data source**:
   - URL: `http://prometheus:9090`
   - Click **Save & Test** → should show “Data source is working ✅”
4. Import ready-made dashboards:
   - **Node Exporter Full (ID: 1860)** → Host metrics
   - **Docker / cAdvisor (ID: 893)** → Container metrics
   - *(Optional)* Create a custom dashboard for Django app metrics.

---

## 📈 Example Metrics

| Metric | Description | Source |
|---------|--------------|--------|
| `node_cpu_seconds_total` | CPU usage per core | Node Exporter |
| `node_memory_MemAvailable_bytes` | Available memory | Node Exporter |
| `container_memory_usage_bytes` | Container memory usage | cAdvisor |
| `django_http_requests_total_by_method_total` | Total HTTP requests | Django Prometheus |
| `django_db_queries_total` | Number of database queries | Django Prometheus |

---

## 🧩 Verification Steps

### ✅ Prometheus Targets
Visit [http://localhost:9090/targets](http://localhost:9090/targets)  
All targets should show **`UP`**:
- `prometheus`
- `node-exporter`
- `cadvisor`
- `django-app`

### ✅ Metrics Endpoints
| Service | URL |
|----------|-----|
| Prometheus | [http://localhost:9090/metrics](http://localhost:9090/metrics) |
| Node Exporter | [http://localhost:9100/metrics](http://localhost:9100/metrics) |
| cAdvisor | [http://localhost:8080/metrics](http://localhost:8080/metrics) |
| Django | [http://localhost:8000/metrics](http://localhost:8000/metrics) |

### ✅ Grafana Dashboards
Visualize metrics for:
- System performance
- Docker container stats
- Django app performance (if configured)

---

## 🧾 Logging & Monitoring Summary

| Area | Tool | Description |
|------|------|--------------|
| **System Monitoring** | Node Exporter | Host CPU, memory, network, disk usage |
| **Container Monitoring** | cAdvisor | Resource utilization by Docker containers |
| **App Monitoring** | Django Prometheus | Application-level metrics |
| **Visualization** | Grafana | Dashboards and visual trends |
| **Logging** | Django Logging | Access and error logs stored in `/app/logs/` |

---

## 🧍‍♂️ Member: Alvin
**Main Responsibility:** Monitoring & Logging Integration

### **Tasks Completed**
- Set up **Prometheus** and **Grafana** containers via Docker Compose  
- Integrated **Node Exporter**, **cAdvisor**, and **Django Prometheus**  
- Configured Prometheus scrape targets for all services  
- Verified metrics scraping and connectivity  
- Imported Grafana dashboards for visualization  
- Captured screenshots for the report

---

## 📸 Screenshots (for report)
Attach the following:
1. Prometheus **Targets** page (all UP)
2. Grafana **Node Exporter Dashboard**
3. Grafana **cAdvisor Dashboard**
4. Django `/metrics` endpoint
5. Django logs in `/app/logs/`

---

## 🧩 Next Steps
- Configure **Grafana alerts** (CPU > 80%, memory > 90%)  
- Add **centralized logging** (e.g., Loki or ELK Stack)  
- Extend monitoring for frontend (React metrics)  

---

## 🧰 Tools Used
- **Prometheus**
- **Grafana**
- **Node Exporter**
- **cAdvisor**
- **Django Prometheus**
- **Docker Compose**

---

🟢 *Monitoring system successfully configured and verified.*
