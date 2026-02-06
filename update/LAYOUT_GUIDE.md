# Dashboard Layout Guide

## Visual Structure Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         HERO SECTION                            │
│  Lowryville Intermediêre Skool                                  │
│  Performance Dashboard · Grade R-9 · 2023-2025                  │
│  (Gradient blue background, white text)                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      FILTER CONTROLS                            │
│                                                                 │
│  Year:     [2023] [2024] [2025*] [All Years]                   │
│                                                                 │
│  Quarter:  [Q1] [Q2] [Q3] [Q4*] [All Quarters]                 │
│                                                                 │
│  Grade:    [Dropdown: All Grades ▼]                            │
│                                                                 │
│  * = Active/selected                                           │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                       STATS CARDS                               │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │ 👥       │ │ ✓        │ │ 📊       │ │ 📚       │          │
│  │ 1,204    │ │ 92.0%    │ │ 63.5%    │ │ Grade 9  │          │
│  │ Learners │ │ Pass Rate│ │ Avg Mark │ │ Focus    │          │
│  │ ↑ +8.2%  │ │ ↑ +3.1%  │ │ ↓ -2.4%  │ │          │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                  ENROLLMENT TRENDS CHART                        │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    Bar Chart                              │ │
│  │  160 ┤                                                    │ │
│  │  120 ┤  █  █  █  █  █  █  █  █  █  █                     │ │
│  │   80 ┤  █  █  █  █  █  █  █  █  █  █                     │ │
│  │   40 ┤  █  █  █  █  █  █  █  █  █  █                     │ │
│  │    0 └─┬──┬──┬──┬──┬──┬──┬──┬──┬──┬─                     │ │
│  │        R  1  2  3  4  5  6  7  8  9                       │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                     PASS RATES CHART                            │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    Line Chart                             │ │
│  │ 100% ┤     ___                                            │ │
│  │  75% ┤  __/   \___                                        │ │
│  │  50% ┤ /          \___                                    │ │
│  │  25% ┤/               \___                                │ │
│  │   0% └┬──┬──┬──┬──┬──┬──┬──┬──┬──┬─                     │ │
│  │       R  1  2  3  4  5  6  7  8  9                       │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                 QUARTERLY PROGRESSION CHART                     │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              Multi-line Chart                             │ │
│  │ 100% ┤  ──── Grade R                                      │ │
│  │  75% ┤  ──── Grade 9                                      │ │
│  │  50% ┤  ──── (other grades)                               │ │
│  │  25% ┤                                                    │ │
│  │   0% └┬───────┬───────┬───────┬─                         │ │
│  │       Q1      Q2      Q3      Q4                          │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│               GRADE 9 SUBJECT PERFORMANCE                       │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │         Horizontal Bar Chart                              │ │
│  │  Life Orientation      ████████████████ 70.8%             │ │
│  │  Creative Arts         ███████████████ 70.2%              │ │
│  │  English FAL          ████████████ 63.4%                  │ │
│  │  Afrikaans HL         ███████████ 61.6%                   │ │
│  │  Social Sciences      ████████ 49.1%                      │ │
│  │  Technology           ████████ 47.6%                      │ │
│  │  Economics            ████████ 47.5%                      │ │
│  │  Natural Sciences     ███████ 44.9%                       │ │
│  │  Mathematics          ██████ 36.8%                        │ │
│  │                       0%        50%       100%             │ │
│  │  🔴 Red = <40%  🟡 Yellow = 40-60%  🟢 Green = >60%       │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    SUBJECT ANALYSIS                             │
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐           │
│  │ Mathematics  │ │ Life Science │ │ Creative Arts│           │
│  │ [NEEDS HELP] │ │ [MONITOR]    │ │ [GOOD]       │           │
│  │ 36.8%        │ │ 44.9%        │ │ 70.2%        │           │
│  │ 67 learners  │ │ 67 learners  │ │ 67 learners  │           │
│  │ ↓ -1.0%      │ │ ↑ +2.5%      │ │ ↑ +8.2%      │           │
│  └──────────────┘ └──────────────┘ └──────────────┘           │
│                                                                 │
│  (Grid continues with all subjects for selected grade)         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Section Breakdown

### 1. Hero Section (Top Banner)
**Purpose:** Branding and title  
**Content:**
- School name
- Dashboard description
- Year range covered

**Styling:**
- Blue gradient background
- White text
- Full width
- 60px padding

---

### 2. Filter Controls
**Purpose:** Interactive data filtering  
**Contains:**

#### Year Buttons (Row 1)
- Four buttons: 2023, 2024, 2025, All Years
- Active button highlighted in blue
- Click to filter all charts to that year

#### Quarter Buttons (Row 2)
- Five buttons: Q1, Q2, Q3, Q4, All Quarters
- Active button highlighted in blue
- Click to filter all charts to that quarter
- Works with year selection

#### Grade Dropdown (Row 3)
- Select menu with options:
  - All Grades
  - Foundation Phase (R-3)
  - Intermediate Phase (4-6)
  - Senior Phase (7-9)
  - Individual grades R-9
- Filters charts and subject cards

**Mobile behavior:**
- Stacks vertically
- Full-width buttons
- Larger tap targets

---

### 3. Stats Cards (Key Metrics)
**Purpose:** At-a-glance summary  
**4 Cards showing:**

#### Card 1: Total Learners
- Icon: People
- Big number: 1,204
- Label: "Total Learners"
- Trend: ↑ +8.2% (green if up, red if down)

#### Card 2: Pass Rate
- Icon: Checkmark
- Big number: 92.0%
- Label: "Average Pass Rate"
- Trend: ↑ +3.1%

#### Card 3: Grade Average
- Icon: Bar chart
- Big number: 63.5%
- Label: "Average Grade %"
- Trend: ↓ -2.4%

#### Card 4: Focus Grade
- Icon: Book
- Big text: Grade 9
- Label: "Focus Grade"
- No trend (informational)

**Updates when:**
- Year changes
- Quarter changes
- Grade filter changes

---

### 4. Enrollment Trends Chart
**Type:** Vertical bar chart  
**Purpose:** Show enrollment by grade  

**X-axis:** Grades (R, 1, 2, 3, 4, 5, 6, 7, 8, 9)  
**Y-axis:** Number of learners  
**Bars:** Blue (#00bfff)  

**Updates when:**
- Year changes
- Quarter changes
- Grade filter changes

**Shows:**
- Which grades are biggest/smallest
- Distribution across school

---

### 5. Pass Rates Chart
**Type:** Filled line chart  
**Purpose:** Show pass rate trends across grades  

**X-axis:** Grades (R, 1, 2, 3, 4, 5, 6, 7, 8, 9)  
**Y-axis:** Pass rate percentage (0-100%)  
**Line:** Blue with filled area underneath  
**Smooth:** Yes (tension: 0.4)  

**Updates when:**
- Year changes
- Quarter changes
- Grade filter changes

**Shows:**
- Which grades have high/low pass rates
- Overall trend (improving or declining)

---

### 6. Quarterly Progression Chart
**Type:** Multi-line chart  
**Purpose:** Show Q1→Q2→Q3→Q4 improvement  

**X-axis:** Quarters (Q1, Q2, Q3, Q4)  
**Y-axis:** Pass rate percentage (0-100%)  
**Lines:** One per grade (different colors)  
**Legend:** Shows below chart (if ≤4 grades)  

**Updates when:**
- Year changes (shows quarters for that year)
- Grade filter changes (shows only those grades)

**Shows:**
- Quarterly progression within a year
- Which quarters perform best
- Improvement over time
- Seasonal patterns

**Special feature:**
- If "All Years" selected, shows 2025 by default
- If >4 grades, hides legend to save space

---

### 7. Grade 9 Subject Performance
**Type:** Horizontal bar chart  
**Purpose:** Show subject averages for Grade 9  

**Y-axis:** Subject names  
**X-axis:** Average mark percentage (0-100%)  
**Bars:** Color-coded by performance:
- Red (<40%): Needs help
- Yellow (40-60%): Monitor
- Green (>60%): Good

**Updates when:**
- Year changes (shows that year's Grade 9)
- Does NOT change with grade filter (always Grade 9)

**Shows:**
- Best performing subjects
- Subjects needing intervention
- Overall Grade 9 landscape

**Special notes:**
- Grade 9 is the exit year (most important)
- Subject names shortened (removes "Gr 09")

---

### 8. Subject Analysis (Subject Cards)
**Type:** Grid of cards  
**Purpose:** Detailed subject breakdown  

**Card layout:**
```
┌─────────────────────────┐
│ Mathematics   [NEEDS HELP]
│ 36.8%
│ 67 learners  ↓ -1.0%
└─────────────────────────┘
```

**Each card shows:**
- Subject name
- Performance badge (NEEDS HELP/MONITOR/GOOD)
- Average mark (large number)
- Number of learners
- Trend vs previous year

**Card colors:**
- Red border (<40%)
- Yellow border (40-60%)
- Green border (>60%)

**Grid layout:**
- 3 columns on desktop
- 2 columns on tablet
- 1 column on mobile

**Updates when:**
- Year changes
- Grade filter changes (shows subjects for that grade)

**Shows:**
- All subjects for selected grade
- Performance at a glance
- Year-over-year trends

---

## Color Legend

### Primary Colors
- **#00bfff** (Deep Sky Blue) - Primary actions, headers
- **#87ceeb** (Sky Blue) - Borders, secondary elements
- **#87cefa** (Light Sky Blue) - Accents, hover states
- **#f8f8ff** (Ghost White) - Page background

### Status Colors
- **#51cf66** (Green) - Good performance, positive trends
- **#ffd43b** (Yellow) - Monitor, moderate performance
- **#ff6b6b** (Red) - Needs help, negative trends

### Usage
- Chart bars: Primary blue
- Chart backgrounds: Light blue fade
- Success: Green
- Warning: Yellow
- Danger: Red

---

## Responsive Breakpoints

### Mobile (< 768px)
```
Stats: 2 columns
Filters: Stacked vertically
Buttons: Full width
Charts: 300px height
Subject grid: 1 column
```

### Tablet (769px - 1024px)
```
Stats: 4 columns
Filters: 2 rows
Buttons: Horizontal
Charts: 350px height
Subject grid: 2 columns
```

### Desktop (> 1024px)
```
Stats: 4 columns
Filters: Single row
Buttons: Horizontal
Charts: 400px height
Subject grid: 3 columns
```

---

## Interactive Elements

### Clickable
- Year buttons
- Quarter buttons
- Grade dropdown
- (Future: Chart elements, subject cards)

### Hover Effects
- Buttons: Background change
- Cards: Lift up, shadow increase
- Charts: Tooltips show exact values

### Active States
- Selected buttons: Blue background, white text
- Other elements: Default state

### Touch Feedback
- Mobile: Scale down slightly on press
- Tap targets: Minimum 44px × 44px

---

## Data Display Patterns

### Big Numbers
```
1,204
92.0%
Grade 9
```
- Large font (40-60px)
- Blue color
- Tabular numbers (monospace)

### Trends
```
↑ +8.2%  (green background)
↓ -2.4%  (red background)
```
- Arrow indicates direction
- Percentage shows change
- Background color shows good/bad

### Badges
```
[NEEDS HELP]  (red)
[MONITOR]     (yellow)
[GOOD]        (green)
```
- Uppercase text
- Color-coded background
- Small, compact

### Labels
```
Total Learners
Average Pass Rate
67 learners
```
- Smaller font (12-16px)
- Muted color (70% opacity)
- Descriptive text

---

## Chart Configurations

### All charts use:
- Chart.js library
- Responsive: true
- MaintainAspectRatio: false
- Smooth animations
- Clean axis labels
- No unnecessary grid lines

### Custom for each:
- **Bar charts:** Vertical orientation
- **Line charts:** Filled area, smooth curves
- **Horizontal bars:** For many items (subjects)
- **Multi-line:** Different colors per dataset

---

## White Space & Spacing

### Margins
- Page sides: 20px
- Section gaps: 32-48px
- Card gaps: 20-24px

### Padding
- Large cards: 32-48px
- Medium cards: 24px
- Small cards: 16-20px
- Buttons: 10-14px vertical, 16-20px horizontal

### Mobile adjustments
- Reduce all spacing by 25%
- Minimum 16px margins
- Touch targets stay large

---

## Loading & Error States

### Loading
```
┌─────────────────────────┐
│   Loading data...       │
│   (centered text)       │
└─────────────────────────┘
```

### Error
```
┌─────────────────────────┐
│   Error loading data    │
│   Check console         │
└─────────────────────────┘
```

### No Data
```
┌─────────────────────────┐
│   No data available     │
│   for this selection    │
└─────────────────────────┘
```

---

## Accessibility Notes

### Colors
- All text meets WCAG AA contrast ratios
- Color not sole indicator (also shapes/text)
- Status indicated by text + color

### Interactive
- All buttons keyboard accessible
- Focus states visible
- Logical tab order

### Screen Readers
- Semantic HTML
- ARIA labels where needed
- Alt text for icons (future)

---

## Summary

**Total sections:** 8  
**Interactive elements:** 3 filter types  
**Charts:** 4 main charts  
**Cards:** 4 stat cards + dynamic subject cards  

**Updates on filter change:** Everything  
**Responsive:** Mobile, tablet, desktop  
**Performance:** <100ms chart updates  
**Browser support:** Modern browsers only  

All sections work together to provide a complete view of school performance with interactive filtering.
