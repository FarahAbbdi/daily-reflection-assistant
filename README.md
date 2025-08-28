# Automated Daily Reflection System 📝  

An automated journaling workflow that generates structured daily reflections. The system runs in the background and produces Markdown summaries covering **events, moods, achievements, challenges, risks, and action items**.  

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

- Morning routine  
- Team meeting  
- Work session  
- Lunch with friends  
- Study block / project work  
- Evening workout  

---  

### Daily Mood & Performance  

- **Overall Day Rating:** 🌟 Good  
- **Predominant Mood:** Focused but slightly stressed  

---  

### Achievements  

- Completed key work tasks  
- Attended scheduled meetings/classes  
- Made progress on personal reading goal  

---  

### Issues / Challenges  

- Spent extra time on phone in the morning before starting work  
- Some difficulty staying focused during afternoon study session  

---  

### Risk Indicators  

- [x] Woke up late / Poor morning routine  
- [ ] Procrastination or distractions  
- [ ] Missed deadlines or delayed submissions  
- [ ] High workload or overlapping tasks  
- [ ] Technical issues  
- [ ] Difficulty understanding material  
- [ ] Communication or collaboration issues  
- [ ] No significant risks or blockers  

---  

### Action Items for Tomorrow  

- Prepare notes for upcoming meeting/project check-in  
- Catch up on pending reading/study topics  

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
- Implement long-term trend visualization dashboard
- Add notifications/reminders for reflection prompts  
- Polish form design and embed example responses in README  


## 🌟 Credits

- **Design and Development:** Farah
