🥊 Juez Bot
### Integrated Multimodal System for AI-Assisted Refereeing in Combat Robotics
 
[![Version](https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge)]()
[![Backend](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![IA](https://img.shields.io/badge/AI-Gemini_2.5_Flash-4285F4?style=for-the-badge)]()
[![Database](https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql)]()
[![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi_Zero_2W-C51A4A?style=for-the-badge&logo=raspberry-pi)]()
[![M5Stack](https://img.shields.io/badge/M5Stack-ESP--NOW-orange?style=for-the-badge)]()
[![Paper](https://img.shields.io/badge/IEEE_Access-Published-00629B?style=for-the-badge)]()
 
---
 
## 📌 Project Description
 
**Juez Bot** is an integrated multimodal decision-support system for combat robotics matches designed to support referees in evaluating matches that do not end by knockout (KO) or submission. The system analyzes combat videos, images, and referee inputs to assess aggressiveness, condition, damage, and control for both robots, proposes a winner, and generates a technical justification based on the competition rules. It integrates field terminals, a portable referee module, an official timer, a mobile capture unit, a web application, a backend, a database, and a multimodal AI inference service into a single traceable workflow, while ensuring that the final decision always remains with the human referee through a human-in-the-loop approach.
 
---
 
## 🖼️ Quick System Overview
 
<p align="center">
  <img src="assets/demo.gif" width="80%" alt="Juez Bot system demonstration GIF">
</p>
<p align="center">
  <a href="https://youtu.be/RK5Msci8DQw" target="_blank">
    <img src="https://img.youtube.com/vi/RK5Msci8DQw/hqdefault.jpg" width="75%" alt="Juez Bot demonstration video">
  </a>
</p>
<p align="center"><em>Full demonstration video of the system's operation</em></p>
---
 
## 🔌 System Architecture
 
<p align="center">
  <img src="assets/architecture.png" width="85%" alt="Layered architecture of Juez Bot">
</p>
<p align="center"><em>Figure 1. Layered architecture: field devices, capture, services, persistence, and AI inference.</em></p>
The system is organized into seven layers, designed to reduce coupling between devices and allow components to be replaced without modifying the entire flow:
 
| Layer | Component | Technology | Main responsibility |
|---|---|---|---|
| Operators | Terminal A and Terminal B | AtomS3, physical buttons | Confirm *ready* state, request intervention, and transmit events to the referee |
| Referee control | Referee module | M5Stack Core2, UIFlow, MicroPython | Start, pause, resume, and stop the match; receive states and display alerts |
| Timing | Official timer | Python, PyQt5 | Display regulation time and execute commands from the referee module |
| Acquisition | Juez Bot (mobile unit) | Sphero RVR+, Raspberry Pi Zero 2 W, camera, FFmpeg | Capture video, control recording segments, and transfer the file to the backend |
| Services | Backend | FastAPI, Uvicorn, Pydantic, HTTPX | Expose endpoints, validate requests, and coordinate files, inference, and persistence |
| Presentation | Web application | Jinja2, HTML, CSS, JavaScript | Register robots, upload images, run analysis, query history |
| Persistence | Database | PostgreSQL, psycopg2 | Store matches, evidence, processing times, scores, and decisions |
| Inference | Multimodal engine | Gemini 2.5 Flash via REST API | Evaluate video and reference images according to refereeing criteria |
 
---
 
## 🏟️ Physical Layout in the Arena
 
<p align="center">
  <img src="assets/arena-layout.png" width="75%" alt="Physical layout of the modules in the combat arena">
</p>
<p align="center"><em>Figure 2. Placement of operator terminals, Juez Bot (mobile camera unit), the referee station, and the official timer, with ESP-NOW links.</em></p>
- The two **operator terminals** are located at the outer corners of the arena.
- **Juez Bot**, the mobile capture unit (Sphero RVR+ + Raspberry Pi Zero 2 W + camera), is positioned at an inner corner with a clear line of sight over the entire match.
- The **referee module** (M5Stack Core2) and the **official timer** are located next to the referee's station, connected via serial communication.
- All field links use **ESP-NOW**, without relying on the local WiFi network.
---
 
## 🧠 Multimodal Inference Flow
 
<p align="center">
  <img src="assets/inference-workflow.png" width="70%" alt="Juez Bot multimodal inference flow">
</p>
<p align="center"><em>Figure 3. Inference stages: evidence validation, encoding, prompt construction, rubric-based evaluation, persistence, and referee confirmation.</em></p>
1. **Input validation** — checks video/image availability and type.
2. **Media encoding** — the video is encoded for transmission to the multimodal service.
3. **Prompt construction** — unambiguous robot identification, area rules, and comparison instructions.
4. **AI multimodal inference** — Gemini 2.5 Flash evaluates the full match.
5. **Structured response analysis** — validation via regular expressions and ranges.
6. **Criteria extraction** — aggressiveness, damage, control, and condition.
7. **Winner proposal**.
8. **Persistence** — stored in PostgreSQL, with the full original response for traceability.
9. **Web presentation** of the result.
10. **Referee confirmation** — final human decision.
---
 
## 🧩 Technologies Used
 
| Technology | Version | Application |
|---|---|---|
| Python | 3.x | Capture, timing, and backend |
| FastAPI | 0.136.1 | Asynchronous REST API |
| Uvicorn | 0.46.0 | ASGI server |
| Pydantic | 2.13.4 | Data validation |
| Jinja2 | 3.1.6 | Interface rendering |
| PostgreSQL | 9.4 | Persistence |
| psycopg2 | 2.9.12 | SQL connection |
| Gemini | 2.5 Flash | Multimodal inference |
| HTTPX | 0.28.1 | Inter-service communication |
| M5Stack AtomS3 / Core2 | — | Operator terminals and referee module |
| ESP-NOW | — | Wireless field communication |
| Sphero RVR+ | — | Mobile platform for the capture unit |
| FFmpeg | — | Video encoding (H.264, MP4) |
| PyQt5 | — | Referee clock with serial communication |
| Render | — | Backend deployment |
 
---
 
## 🚀 Main Features
 
| Feature | Description |
|---|---|
| 🎥 Mobile capture | Match recording via Sphero RVR+ + Raspberry Pi Zero 2 W + camera. |
| 🔴 Remote recording control | Start, pause, resume, and stop, synchronized with the referee. |
| 🤖 Multimodal analysis | Evaluation of video and initial/final images via Gemini 2.5 Flash. |
| 🥋 Rubric-based evaluation | Technical scoring on aggressiveness, condition, damage, and control. |
| 🏷️ Robot identification | Unambiguous recognition of Robot A / Robot B by name and images. |
| 🖥️ Web interface | Robot registration, evidence upload, results, and technical review. |
| 🗄️ Traceable history | Full record in PostgreSQL, including the model's original response. |
| 📡 Physical modules | AtomS3 terminals and M5Stack Core2 referee module via ESP-NOW. |
| ⏱️ Official clock | Independent timer in PyQt5 with serial commands. |
| 🧑‍⚖️ Human-in-the-loop | The system proposes; the human referee confirms or corrects the final decision. |
 
---
 
## 🚦 Evaluation Engine
 
Each robot is evaluated with a maximum score of **40 points**:
 
| Criterion | Max score | Description |
|---|---:|---|
| Aggressiveness | 15 | Offensive initiative, pressure, and pursuit of contact. |
| Condition | 5 | Physical and functional state at the end of the match. |
| Damage | 10 | Visible damage inflicted on the opponent. |
| Control | 10 | Arena dominance, orientation, pushing power, and tactical positioning. |
 
The winner is determined by total score; in case of a tie, the tiebreaker order is damage → aggressiveness → control → condition. A tie is only considered when there is no effective contact or clear offensive pressure.
 
---
 
## 📊 Validation Results (IEEE Access)
 
Validated across two scenarios: 30 historical matches from the **BrettZone-NHRL** repository and 20 matches with judge decisions from the **IEEE Pumabot 2026** event.
 
| Scenario | n | Accuracy (Acc.) | 95% CI (Wilson) | Bal. Acc. | Macro F1 | MCC |
|---|---:|---:|---|---:|---:|---:|
| BrettZone–NHRL | 30 | 86.7% | 70.3–94.7% | 86.1% | 86.1% | 0.722 |
| IEEE Pumabot 2026 | 20 | 90.0% | 69.9–97.2% | 89.0% | 89.0% | 0.780 |
| **Combined** | 50 | **88.0%** | 76.2–94.4% | 87.3% | 87.3% | 0.745 |
 
### 🎯 Combined confusion matrix
 
| | Predicted A | Predicted B |
|---|---:|---:|
| **Official A** | 28 | 3 |
| **Official B** | 3 | 16 |
 
Errors were symmetric (3 in each direction), showing no evidence of positional bias toward A or B.
 
### ⚖️ Normalized criterion contribution (combined dataset)
 
| Criterion | Contribution |
|---|---:|
| Control | 33.6% |
| Aggressiveness | 32.3% |
| Damage | 21.7% |
| Condition | 12.4% |
 
The average margin between scores was **14.80 points**. Five of the six disagreements had margins ≥11 points, confirming that a wide margin **should not** be interpreted as calibrated confidence — hence the importance of keeping the referee in the decision loop.
 
### 🗳️ End-to-end functional tests
 
| Code | Test | Documented result |
|---|---|---|
| F1 | Operator signaling | States and alerts displayed on the M5Stack Core2 |
| F2 | Timer control | Serial commands correctly interpreted by the PyQt5 clock |
| F3 | Capture synchronization | Recording (start/pause/resume/stop) verified |
| F4 | Evidence transfer | Videos and images received without critical errors |
| F5 | Multimodal inference | Response with winner and technical scores received and displayed |
| F6 | Persistence and history | Results stored in PostgreSQL and queryable |
| F7 | Event deployment | Joint operation of physical and logical modules during IEEE Pumabot 2026 |
 
---
 
## 📡 Communication Between Modules
 
| Source | Destination | Channel | Data | Purpose |
|---|---|---|---|---|
| Terminals A/B | Referee module | ESP-NOW | Ready, alert, or submission codes | Coordinate competitor status and request intervention |
| Referee module | Official timer | Serial | Start, pause, resume, stop | Control regulation time from the portable device |
| Backend | Juez Bot | HTTP GET | Recording and pause states | Synchronize capture with referee actions |
| Juez Bot | Backend | HTTP multipart | MP4 video and metadata | Transfer audiovisual evidence |
| Web application | Backend | HTTP multipart | Identifiers, video, initial/final images | Register the match and request inference |
| Backend | AI service | HTTPS / JSON | Instructions and encoded files | Run multimodal analysis |
| Backend | PostgreSQL | SQL | Evidence, scores, times, states | Ensure persistence and traceability |
| Backend | Web application | HTTP / JSON | Result, explanation, history | Support review and referee confirmation |
 
---
 
## 🔄 Operational Sequence
 
1. Each operator confirms that their robot is ready.
2. Once both states are valid, the referee starts the timer and recording.
3. During the match, terminals can send alerts; the referee can pause or stop.
4. At the end, Juez Bot transfers the video and any available final images are added.
5. The backend validates the evidence and builds the multimodal request.
6. If KO or submission is confirmed, the **direct rule** applies (bypassing the AI model).
7. If the match reaches the time limit, **multimodal analysis** is executed.
8. The system extracts the proposed winner and per-criterion scores.
9. The result is stored in PostgreSQL along with the model's original response.
10. The interface presents the result; the referee confirms or corrects the final decision.
### 🔁 Match state model
 
`waiting` → `ready` → `recording` ⇄ `paused` → `finished` → `processing` → `result available` → `validated`
 
---
 
## 🌐 API Endpoints
 
| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Displays the main interface. |
| `/health` | GET | Checks the backend status. |
| `/upload` | POST | Uploads the video recorded by Juez Bot. |
| `/analyze` | POST | Analyzes video and images with multimodal AI. |
| `/historial` | GET | Queries the most recent stored results. |
| `/check_status` | GET | Checks whether a video is available for analysis. |
| `/start_recording` | GET | Starts remote recording. |
| `/pause_recording` | GET | Pauses remote recording. |
| `/resume_recording` | GET | Resumes remote recording. |
| `/stop_recording` | GET | Stops remote recording. |
| `/recording_status` | GET | Queries the current recording status. |
 
---
 
## ⚙️ Installation
 
```bash
git clone https://github.com/PatrickZ29/RobotVisionIA.git
cd RobotVisionIA
python -m venv venv
```
 
On Windows:
```bash
venv\Scripts\activate
```
 
On Linux or macOS:
```bash
source venv/bin/activate
```
 
```bash
pip install -r requirements.txt
```
 
---
 
## 🔐 Environment Variable Configuration
 
```env
GEMINI_API_KEY=place_your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
 
VIDEO_FOLDER=videos
 
DB_HOST=localhost
DB_PORT=5432
DB_NAME=robot_ai
DB_USER=postgres
DB_PASSWORD=1234
```
 
For deployment on Render or similar services:
```env
DATABASE_URL=postgresql://user:password@host:5432/database_name
```
 
> ⚠️ It is not recommended to upload `.env` files or private keys to the repository.
 
---
 
## ▶️ Running the Backend
 
```bash
uvicorn main:app --reload
```
 
```text
http://localhost:8000
http://localhost:8000/health
```
 
---
 
## ☁️ Deployment
 
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```
 
```env
GEMINI_API_KEY=gemini_key
GEMINI_MODEL=gemini-2.5-flash
DATABASE_URL=postgresql_url
VIDEO_FOLDER=videos
```
 
---
 
## 🛡️ Security
 
```gitignore
venv/
.env
__pycache__/
*.pyc
uploads/
videos/
*.log
.DS_Store
.api_keys.py
```
 
- Do not upload `.env` files or Gemini keys to the repository.
- Do not include real credentials in `config.py`.
- Keep `videos/`, `uploads/`, and temporary files out of Git.
---
 
## 🌱 Limitations and Future Work
 
- [ ] Synchronized cameras to associate each criterion with specific temporal evidence.
- [ ] Repeated inference to measure stability and confidence calibration.
- [ ] Comparison across models and prompts (committee-style arbitration, e.g., EvalCouncil style).
- [ ] Partial edge inference to reduce dependence on Internet connectivity.
- [ ] Validated JSON schemas for model responses.
- [ ] Evaluation of availability, ESP-NOW packet loss, and cost per match.
- [ ] Understandable appeal and review mechanisms for competitors and organizers.
---
 
## 👤 Author
 
**Patrick Neil Zamora Lascano**
Universidad Tecnológica Indoamérica
Information Technology Engineering Program
 
---
 
## 📄 License
 
This project was developed for academic purposes as part of the degree thesis related to the intelligent refereeing system for combat robotics, validated during the **IEEE Pumabot 2026** event.
 
⭐ Academic project in applied multimodal AI, IoT, and intelligent sports refereeing