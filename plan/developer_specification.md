# Lowryville Intermediate School
## Data Visualization Web Experience - Developer Specification

**School:** Lowryville Intermediêre Skool  
**EMIS:** 300023304  
**District:** Pixley-Ka-Seme  
**Province:** Northern Cape  
**Grades:** R - 9

---

## Color Scheme

```css
--primary-blue: #00bfff;      /* rgb(0,191,255) - Deep Sky Blue */
--secondary-blue: #87ceeb;    /* rgb(135,206,235) - Sky Blue */
--accent-blue: #87cefa;       /* rgb(135,206,250) - Light Sky Blue */
--background: #f8f8ff;        /* rgb(248,248,255) - Ghost White */
--text-dark: #2c3e50;         /* For readability */
--text-light: #ffffff;        /* White text on blue */
```

**Usage:**
- Primary buttons, headers, highlights: `#00bfff`
- Cards, borders, secondary elements: `#87ceeb`
- Hover states, accents: `#87cefa`
- Page background: `#f8f8ff`

---

## What We're Building

A modern, clean dashboard to showcase 3 years of school performance data (2023, 2024, 2025). The experience should feel professional but approachable—think Apple's education section meets clean government data portals.

---

## Data We Have

### 1. **School Profile**

```json
{
  "staff": {
    "total": 36,
    "principal": 1,
    "deputy_principals": 2,
    "department_heads": 5,
    "post_level_1": 28
  },
  "infrastructure": {
    "challenges": [
      "Toilets need maintenance",
      "No school hall",
      "Need financial aid"
    ]
  },
  "enrollment": {
    "grades": ["R", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "years_covered": ["2023", "2024", "2025"]
  }
}
```

**Display as:**
- Simple stat cards at the top
- Staff breakdown pie chart
- Infrastructure needs list (bullet points, non-intrusive)

---

### 2. **Enrollment Data** (2023-2025)

Per quarter, per grade, per year. Shows how many kids in each grade over time.

**What to show:**
- **Line graph:** Enrollment trends per grade across years
- **Bar chart:** Year-over-year comparison (2023 vs 2024 vs 2025)
- **Stacked area chart:** Total school enrollment broken down by grade

**Key metrics:**
- Total enrollment per year
- Growth/decline percentages
- Biggest/smallest grades

---

### 3. **Pass Rates** (2023-2025)

Overall pass percentage per grade, tracked quarterly.

**What to show:**
- **Line graph:** Pass rate trends by grade (show improvement/decline)
- **Heatmap:** Grades (rows) × Years (columns), color-coded by pass %
  - Green for 80%+
  - Yellow for 60-79%
  - Red for <60%
- **Progress cards:** Q1 → Q2 → Q3 → Q4 progression for each year

**Key metrics:**
- School-wide pass rate per year
- Best/worst performing grades
- Quarter with highest improvement

---

### 4. **Grade Averages** (2023-2025)

Average percentage mark per grade, per quarter.

**What to show:**
- **Bar chart:** Grade averages side-by-side (2023 vs 2024 vs 2025)
- **Radar chart:** Multi-year comparison showing all grades at once
- **Mini sparklines:** Next to each grade showing trend over quarters

**Key metrics:**
- Highest average grade
- Lowest average grade
- Year-over-year improvement

---

### 5. **Subject Performance** (Detailed)

For each grade, for each year, we have:
- Average mark per subject
- How many kids in each achievement band (Level 1-7)
- Total learners taking each subject

**Achievement Levels:**
- Level 1: 0-29% (Failing)
- Level 2: 30-39% (Weak)
- Level 3: 40-49% (Borderline)
- Level 4: 50-59% (Pass)
- Level 5: 60-69% (Good)
- Level 6: 70-79% (Very Good)
- Level 7: 80-100% (Excellent)

**What to show:**

#### Grade 9 Deep Dive (Exit Year - Most Important)
- **Horizontal bar chart:** Subject averages sorted high to low
- **Stacked bar chart:** Achievement distribution per subject
  - Each bar = one subject
  - Segments = how many kids at each level
  - Color-coded: Red (Level 1-2), Yellow (Level 3), Green (Level 4-7)
- **Table view:** Sortable by subject, average, pass rate
- **Year comparison:** Show 2023 vs 2024 vs 2025 for Grade 9

#### All Other Grades
- **Subject cards:** Grid layout, each subject is a card showing:
  - Subject name
  - Average mark (big number)
  - Achievement distribution (mini bar chart)
  - Trend arrow (↑ or ↓ vs previous year)
- **Filter by grade:** Dropdown to switch between Grade R-9

**Key metrics:**
- Best performing subject school-wide
- Worst performing subject (needs intervention)
- Subjects with most Level 1-2 students (red flag)

---

### 6. **Year-over-Year Comparisons**

Side-by-side comparisons of everything.

**What to show:**
- **Delta cards:** 
  - "Enrollment: +12% from 2023 to 2024"
  - "Pass rate: -3% from 2024 to 2025"
- **Comparison sliders:** Drag to see 2023 vs 2024 vs 2025 data
- **Growth indicators:** ↑ Green for positive, ↓ Red for negative

---

## Page Structure

### Landing View (Hero Section)
```
┌─────────────────────────────────────────┐
│  🏫 Lowryville Intermediate School      │
│  Grade R-9 • 2023-2025 Performance      │
│                                         │
│  [1,143]  [92%]   [36]   [Grade 9]     │
│  Learners Pass   Staff   Exit Focus    │
│  (2025)   Rate                          │
└─────────────────────────────────────────┘
```

### Main Dashboard Sections

1. **Overview** (default view)
   - Big numbers (enrollment, pass rates, staff)
   - Quick wins (top subjects, best grades)
   - Year selector (2023 | 2024 | 2025)

2. **Enrollment Trends**
   - Interactive line/bar charts
   - Grade breakdown
   - Quarterly progression

3. **Academic Performance**
   - Pass rates heatmap
   - Grade averages
   - Quarterly improvements

4. **Subject Analysis**
   - Grade 9 spotlight
   - All grades subject cards
   - Achievement distributions

5. **Year Comparisons**
   - Side-by-side metrics
   - Growth/decline indicators
   - Quarterly breakdowns

6. **School Profile**
   - Staff structure
   - Infrastructure needs
   - Contact/admin info

---

## Tech Stack (Recommended)

### Frontend Framework
**Next.js 14+ (React)** or **SvelteKit**
- Fast, modern, SEO-friendly
- Server-side rendering for quick loads
- Easy to deploy (Vercel/Netlify)

### Charts & Visualizations
**Recharts** or **Chart.js** with **react-chartjs-2**
- Clean, customizable
- Works great with your color scheme
- Responsive out of the box

Alternative: **D3.js** if you want more control

### UI Components
**Tailwind CSS** + **shadcn/ui** or **Headless UI**
- Matches your minimalist vibe
- Easy to customize colors
- Pre-built components (cards, dropdowns, etc.)

### State Management
**Zustand** or **React Context** (if using React)
- Simple, no boilerplate
- Perfect for filter states (year selector, grade filters)

### Data Handling
**JSON files** (static) or **API endpoints**
- Pre-process data into clean JSON
- No database needed for static reports
- Can add API later if needed

---

## Chart Types by Section

| Data Type | Visualization | Why |
|-----------|---------------|-----|
| Enrollment over time | Line graph | Shows trends clearly |
| Enrollment by grade | Stacked bar chart | Easy comparison |
| Pass rates by grade | Heatmap | Quick pattern spotting |
| Pass rate trends | Line graph | Track progress |
| Grade averages | Horizontal bars | Easy to compare |
| Subject performance | Stacked bars | Shows distribution |
| Achievement levels | Donut/pie chart | Proportions clear |
| Year comparisons | Grouped bar chart | Side-by-side wins |

---

## Interaction Design

### Filters
- **Year selector:** Tabs or dropdown (2023, 2024, 2025, All)
- **Grade selector:** Dropdown (R, 1, 2...9, All)
- **Quarter selector:** Buttons (Q1, Q2, Q3, Q4, Year-end)

### Hover States
- Cards lift slightly (shadow increase)
- Chart tooltips show exact numbers
- Color shift to accent blue

### Responsive Breakpoints
```css
Mobile:  < 640px  (1 column, stacked charts)
Tablet:  640-1024px  (2 columns)
Desktop: > 1024px  (3-4 column grid)
```

---

## Data Structure for Developers

All data is extracted and ready in JSON format. Here's the structure:

```json
{
  "school_info": {
    "name": "Lowryville Intermediêre Skool",
    "emis": "300023304",
    "staff": {
      "total": 36,
      "breakdown": {...}
    }
  },
  "years": {
    "2023": {
      "quarters": {
        "Q1": {
          "enrollment": {"Grade_R": 78, "Grade_1": 159, ...},
          "pass_rates": {"Grade_R": 100, "Grade_1": 64.78, ...},
          "grade_averages": {"Grade_R": 69.79, ...}
        },
        "Q2": {...},
        "Q3": {...},
        "Q4": {...}
      },
      "subjects": {
        "Grade_9": [
          {
            "name": "Mathematics (Gr 09)",
            "average_mark": 29.0,
            "achievement_distribution": {
              "Level_1": 35,
              "Level_2": 0,
              "Level_3": 8,
              "Level_4": 1,
              "Level_5": 0,
              "Level_6": 0,
              "Level_7": 0
            },
            "total_learners": 44
          },
          ...
        ]
      }
    },
    "2024": {...},
    "2025": {...}
  }
}
```

---

## Visual Style Guidelines

### Typography
- **Headings:** Inter, SF Pro, or Poppins (modern, clean)
- **Body:** System font stack or Inter
- **Numbers:** Tabular numbers (monospace) for alignment

### Cards
```css
.stat-card {
  background: white;
  border: 1px solid #87ceeb;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 191, 255, 0.1);
}

.stat-card:hover {
  box-shadow: 0 4px 16px rgba(0, 191, 255, 0.2);
  transform: translateY(-2px);
  transition: all 0.3s ease;
}
```

### Chart Colors
Primary dataset: `#00bfff`  
Comparison dataset: `#87ceeb`  
Highlight/accent: `#87cefa`  
Negative/warning: `#ff6b6b`  
Positive/success: `#51cf66`

### Spacing
- Section gaps: 48px
- Card gaps: 24px
- Internal padding: 16-24px
- Mobile: Reduce by 25%

---

## Performance Goals

- **Initial load:** < 2 seconds
- **Chart render:** < 500ms
- **Filter changes:** Instant (< 100ms)
- **Mobile-friendly:** Fully responsive
- **Accessibility:** WCAG AA compliant

---

## Deployment

**Recommended:** Vercel or Netlify
- One-click deploy from GitHub
- Automatic HTTPS
- CDN included
- Free tier available

---

## Summary

You're building a clean, professional data dashboard that:
- Shows 3 years of school performance
- Makes it easy to spot trends and problems
- Focuses on Grade 9 (your exit year)
- Uses your school colors throughout
- Works on phones, tablets, and desktops
- Loads fast and looks sharp

All the data is ready in JSON. Just plug it into charts and build the interface around your color scheme. Keep it minimal—let the data tell the story.
