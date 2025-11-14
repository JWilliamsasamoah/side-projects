# NHL Real-Time Shot Attempt Bot and GOALS

This project connects to the **NHL SMT Optics3D tracking API**, pulls **live game events**, and posts **shot attempt and Goals updates to Twitter** in real time.

It’s a side project that builds on my experience as a **Data Engineer Intern at MLSE**, working with real-time puck and player tracking data.

---

## 🔍 What This Project Does

- Authenticates with the SMT Optics3D (NHL) API using a username/password login.
- Finds a specific NHL game using:
  - Date (e.g., `2022_05_02`)
  - Home team (e.g., `TOR`)
  - Away team (e.g., `TBL`)
- Uses the `GameSchedule` endpoint to get:
  - `gameID`
  - `gameStartUTC`
  - `gameEndUTC`
- Calls the **MarkerActivity** endpoint with `MinorType=EventShot` to pull live event data.
- Filters events for `"Shot Attempt"` using **Pandas**.
- Automatically tweets the latest shot attempt description using the **Twitter API** inside a loop.

---

## 🛠 Tech Stack

**Language:**
- Python

**Libraries:**
- `requests`
- `pandas`
- `numpy`
- `matplotlib`, `matplotlib.animation`
- `opencv-python` (`cv2`)
- `requests-oauthlib`
- `time`, `datetime`, `json`, `os`, `warnings`

**APIs:**
- SMT Optics3D NHL endpoints
- Twitter API v2

---

## 🚀 Getting Started

> ⚠️ You must have valid credentials for both:
> - SMT Optics3D (NHL tracking)
> - Twitter API (keys & tokens)

1. **Clone the repo and go to the NHL folder:**

   ```bash
   git clone https://github.com/JWilliamsasamoah/side-projects.git
   cd side-projects/NHL
