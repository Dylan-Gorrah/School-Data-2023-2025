# Lowryville School Performance Dashboard

📊 **Interactive School Performance Analytics Dashboard**  
📅 **Data Coverage:** 2023-2025 Academic Years  
🎓 **Grades:** R (Reception) through Grade 9  
📱 **Fully Responsive:** Desktop, Tablet & Mobile Optimized

---

## 🚀 **Live Demo**
**Access the dashboard here:**  
👉 [https://dylan-gorrah.github.io/School-Data-2023-2025/](https://dylan-gorrah.github.io/School-Data-2023-2025/)

---

## ✨ **Key Features**

### 📈 **Interactive Filtering**
- **Year Selection:** 2023, 2024, 2025, or All Years comparison
- **Quarterly Analysis:** Q1, Q2, Q3, Q4 breakdown  
- **Grade Filtering:** Individual grades or phases (Foundation, Intermediate, Senior)
- **Real-time Updates:** All charts update instantly when filters change

### 📊 **Comprehensive Analytics**
- **Enrollment Trends:** Student distribution across grades
- **Pass Rate Analysis:** Performance tracking with trend indicators
- **Quarterly Progression:** Q1→Q4 improvement visualization
- **Subject Performance:** Detailed subject breakdown with alerts
- **Grade 9 Focus:** Exit year subject analysis with color-coded performance

### 🎨 **Visual Features**
- **Modern UI:** Clean, professional design with blue theme
- **Color-Coded Alerts:**
  - 🟢 **GOOD** (>60% average)
  - 🟡 **MONITOR** (40-60% average)  
  - 🔴 **NEEDS ATTENTION** (<40% average)
- **Growth Indicators:** ↑↓ arrows showing year-over-year changes
- **Interactive Charts:** Hover tooltips, smooth animations

### 📱 **Responsive Design**
- **Desktop:** Full-featured multi-column layout
- **Tablet:** Optimized for Samsung Tab A9 (1340x800)
- **Mobile:** Touch-friendly interface with larger tap targets

---

## 📁 **Project Structure**

```
School-Data-2023-2025/
├── index.html                    # Main dashboard (GitHub Pages entry point)
├── school_data.json             # Enrollment & pass rate data
├── subject_data_complete.json   # Subject performance + staff data
├── img/
│   └── logo.png                 # School logo
├── enhanced_dashboard.html      # Full dashboard (alternative access)
├── school_dashboard.html        # Original dashboard (legacy)
└── README.md                    # This file
```

---

## 🛠 **Technology Stack**

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Charts:** Chart.js (via CDN)
- **Styling:** CSS Grid, Flexbox, CSS Custom Properties
- **Data:** JSON format for fast loading
- **Hosting:** GitHub Pages (static site)

---

## 📊 **Data Coverage**

### **Academic Years:** 2023, 2024, 2025
### **Grades:** R, 1, 2, 3, 4, 5, 6, 7, 8, 9
### **Subjects Per Grade:**
- **Foundation Phase (R-3):** Mathematics, Home Language, Life Skills, First Additional Language
- **Intermediate Phase (4-6):** Natural Sciences, Social Sciences, Technology, Creative Arts
- **Senior Phase (7-9):** Economics, Life Orientation, plus all intermediate subjects

### **Staff Data Included:**
- Principal, Deputy Principal, Department Heads
- Teachers, Support Staff, Administrative Staff
- Year-over-year staffing trends (2023-2025)

---

## 🎯 **How to Use**

1. **Visit the Dashboard:** [Live Demo Link](https://dylan-gorrah.github.io/School-Data-2023-2025/)
2. **Select Year:** Click year buttons (2023/2024/2025/All Years)
3. **Filter Quarter:** Choose Q1/Q2/Q3/Q4 for quarterly analysis
4. **Choose Grade:** Select individual grade or phase from dropdown
5. **View Analytics:** Charts update automatically with filtered data
6. **Subject Analysis:** Scroll down for detailed subject performance cards

---

## 🔧 **Technical Implementation**

### **Data Flow:**
```
User Interaction → Filter Update → Data Aggregation → Chart Re-render
```

### **Key Functions:**
- `updateDashboard()` - Master refresh function
- `getFilteredData()` - Data filtering based on selections
- `updateSubjectCards()` - Dynamic subject card generation
- `calculateTrends()` - Year-over-year comparison logic

### **Performance Features:**
- **Fast Loading:** <2 seconds initial load
- **Instant Updates:** <100ms chart refresh
- **Memory Efficient:** Chart destruction prevents leaks
- **Mobile Optimized:** Touch events, smooth scrolling

---

## 📱 **Mobile & Tablet Support**

### **Responsive Breakpoints:**
- **Mobile (<768px):** Single column, stacked filters
- **Tablet (769-1024px):** Two columns, optimized for Tab A9
- **Desktop (>1024px):** Full multi-column layout

### **Touch Features:**
- **Tap Targets:** Minimum 44px × 44px
- **Touch Feedback:** Scale animations on press
- **Smooth Scrolling:** Optimized vertical scrolling
- **No Text Selection:** Clean touch interaction

---

## 🎨 **Design System**

### **Colors:**
- **Primary Blue:** #00bfff (actions, headers)
- **Secondary Blue:** #87ceeb (borders, accents)
- **Success Green:** #51cf66 (good performance)
- **Warning Yellow:** #ffd43b (monitoring needed)
- **Danger Red:** #ff6b6b (needs attention)

### **Typography:**
- **Font:** -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter'
- **Weights:** 400 (regular), 600 (semibold), 700 (bold)
- **Responsive:** clamp() for fluid sizing

---

## 📈 **Data Insights Available**

### **Performance Tracking:**
- Grade-level pass rates over time
- Subject performance trends
- Quarterly progression analysis
- Year-over-year comparisons

### **Enrollment Analytics:**
- Student distribution by grade
- Growth trends across years
- Class size planning insights

### **Subject Deep Dives:**
- Average marks per subject
- Achievement level distributions
- Performance alerts and trends
- Grade 9 exit analysis

---

## 🚀 **Deployment**

This project is deployed using **GitHub Pages** for free, secure hosting:

- **Automatic Deployment:** Updates push to GitHub → Live in minutes
- **HTTPS Security:** SSL certificate included
- **Global CDN:** Fast loading worldwide
- **Version Control:** Full Git history of changes

---

## 📞 **Support & Information**

### **School Details:**
- **Name:** Lowryville Intermediêre Skool
- **Grades:** R (Reception) through Grade 9
- **Data Period:** 2023-2025 Academic Years
- **Dashboard Purpose:** Performance analytics & improvement tracking

### **Technical Support:**
- **Browser Support:** Chrome 90+, Safari 14+, Firefox 88+, Edge 90+
- **Mobile Support:** iOS Safari, Chrome Mobile
- **Requirements:** JavaScript enabled, modern browser

---

## 🔄 **Updates & Maintenance**

### **Data Updates:**
- Annual data addition (2026, 2027, etc.)
- Quarterly performance updates
- Staff data adjustments
- New subject integration

### **Feature Enhancements:**
- Additional chart types
- Export functionality (PDF/Excel)
- Advanced filtering options
- Comparison tools

---

## 📄 **License & Usage**

This dashboard is intended for educational performance analysis and improvement planning at Lowryville Intermediêre Skool.

**Data Privacy:** All student data is anonymized and aggregated for performance analysis purposes only.

---

*Last Updated: February 2026*  
*Dashboard Version: 2.0 Enhanced*  
*Data Coverage: 2023-2025 Academic Years*
