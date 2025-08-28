# Automated Daily Reflection System 📝  

An automated journaling workflow that generates structured daily reflections.  
The system runs in the background and produces Markdown summaries covering **events, moods, achievements, challenges, risks, and action items**.  

⚠️ **Note:** This project is a work in progress. The automation logic (via `launchd`) and full setup instructions will be pushed once finalized.  

---

## ⚙️ How It Works  

Every day, the system automates a full reflection workflow:  

1. **Daily Event Creation**  
   - A new calendar event is automatically created with a link to a reflection form.  
   - The user clicks into the event and fills out the form at their convenience.  

2. **Input Collection**  
   - Daily events are pulled from Google Calendar.  
   - Reflection responses are collected from the attached Google Form.  

3. **Processing & Analysis**  
   - A scheduled `launchd` job runs later in the day.  
   - OpenAI API analyzes the reflection responses and daily calendar events.  
   - Both are combined into a structured Markdown summary.  

4. **Output**  
   - Markdown files are generated with sections for events, mood, achievements, challenges, risks, and action items.  
   - Over time, entries can be aggregated to highlight **trends, habits, and blockers**.  

---

## 🧰 Tech Highlights  

- **Automation**: macOS `launchd` for daily job scheduling  
- **APIs**: Google Calendar + Google Sheets APIs for events and input collection  
- **AI**: OpenAI API for natural language analysis and structured summaries  
- **Data Format**: Outputs stored as Markdown for easy reading and versioning  

---

## 📝 Example Daily Reflection Output  

Here’s what a generated reflection looks like:  

### Today's Events  

- Wake up  
- SWEN20003 Tutorial 1  
- COMP30023 Lecture 1  
- Social - Black Collective  
- COMP30023 Study Session  
- Gym  

---  

### Daily Mood & Performance  

- **Overall Day Rating:** 🌟 Excellent  
- **Predominant Mood:** Anxious or stressed  

---  

### Achievements  

- Went to all my lectures (IT Project, Models of Computation)  
- Went to gym in the morning  
- Read 10 pages of a book  

---  

### Issues / Challenges  

- Woke up a little later than usual at 9am and spent 30 mins on phone before getting out of bed  

---  

### Risk Indicators  

- [x] Woke up late / Poor morning routine  
- [ ] Procrastination or distractions  
- [ ] Missed deadlines or delayed submissions  
- [ ] High workload or overlapping assignments  
- [ ] Technical issues  
- [ ] Difficulty understanding material  
- [ ] Communication or collaboration issues  
- [ ] No significant risks or blockers  

---  

### Action Items for Tomorrow  

- Prepare for stand-up for group assignment (IT Project)  
- Catch up on lecture for Models of Computation  

---  

### Additional Reflection  

> Placeholder reflection text here.  

---

## 📋 Reflection Form  

👉 [Reflection Input Form](https://docs.google.com/forms/d/1GNRxM97nlvFPppCA9pglgzevJYcDUE0eNdzlX0kD0pE/edit)  

The form is designed to be **quick and lightweight**, with fields for:  
- Daily mood (rating + tags)  
- Achievements  
- Challenges  
- Risks (checklist)  
- Open-ended reflection  

---

## ✅ Roadmap / Future Work  

- Push full codebase with API integrations and automation scripts  
- Add setup instructions (API keys, dependencies, launchd job file)
- Polish form design and embed example responses in README  


## 🌟 Credits

- **Design and Development:** Farah
