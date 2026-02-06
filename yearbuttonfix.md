# Year Button Fix Requirements

## Current Issue
Year selector buttons are not working - clicking them does not filter chart data by year.

## End Goal Requirements

### 1. Year Button Functionality
- When clicking "2023" button → Display ONLY 2023 data on all charts
- When clicking "2024" button → Display ONLY 2024 data on all charts  
- When clicking "2025" button → Display ONLY 2025 data on all charts
- When clicking "All Years" button → Display comparison of all three years

### 2. Quarterly Button Functionality (New Requirement)
- Add quarterly selector buttons: Q1, Q2, Q3, Q4
- When clicking a quarter → Display data for that specific quarter
- Should work in combination with year selection
- Example: Click "2024" + "Q2" → Show Q2 2024 data only

### 3. Visual Feedback
- Active button highlighting for selected year/quarter
- Smooth chart transitions when switching between years/quarters
- Clear indication of current selection

## Files Responsible for Button & Graph Functionality

### Primary Files:
1. **plan/visual_mockup.html** - Main dashboard file
   - Contains HTML structure for year buttons
   - Contains JavaScript for button event handling
   - Contains Chart.js implementations
   - Contains data structures (schoolData, subjectData)

### Supporting Files:
2. **plan/school_data.json** - Raw school data
   - Contains enrollment, pass rates, grade averages
   - Organized by year → quarter → grade
   - Source data for chart updates

3. **New/subject_data_complete.json** - Subject performance data
   - Contains detailed subject data for 2023-2025
   - Achievement distributions (Level 1-7)
   - Can be integrated for enhanced subject charts

## Technical Implementation Notes

### Year Button Structure (HTML):
```html
<div class="year-selector">
    <button class="year-btn" data-year="2023">2023</button>
    <button class="year-btn" data-year="2024">2024</button>
    <button class="year-btn" data-year="2025">2025</button>
    <button class="year-btn active" data-year="all">All Years</button>
</div>
```

### Required Quarterly Button Structure (HTML):
```html
<div class="quarter-selector">
    <button class="quarter-btn" data-quarter="Q1">Q1</button>
    <button class="quarter-btn" data-quarter="Q2">Q2</button>
    <button class="quarter-btn" data-quarter="Q3">Q3</button>
    <button class="quarter-btn active" data-quarter="Q4">Q4</button>
</div>
```

### JavaScript Functions to Fix:
1. **setupYearButtons()** - Event listeners for year buttons
2. **updateEnrollmentChart()** - Filter enrollment data by year/quarter
3. **updatePassRateHeatmap()** - Filter pass rate data by year/quarter
4. **updateGrade9SubjectsChart()** - Filter subject data by year
5. **updateAllGradesSubjectCharts()** - Filter all subject charts

### Data Structure Access:
```javascript
// Current data access pattern:
schoolData.summary['2024'].quarters.Q4.enrollment['Grade_7']
schoolData.summary['2024'].quarters.Q4.pass_rates['Grade_7']

// Required quarterly filtering:
schoolData.summary[selectedYear].quarters[selectedQuarter].enrollment['Grade_X']
schoolData.summary[selectedYear].quarters[selectedQuarter].pass_rates['Grade_X']
```

## Feasibility Assessment

### ✅ **POSSIBLE - Year Button Fix**
- Data structure supports year-based filtering
- Chart.js supports dynamic data updates
- Event handling infrastructure exists
- Just needs proper implementation

### ✅ **POSSIBLE - Quarterly Button Addition**  
- Data structure includes quarterly data (Q1, Q2, Q3, Q4)
- Can add quarterly selector alongside year selector
- Requires additional JavaScript for quarter filtering
- More complex but definitely achievable

### Implementation Priority:
1. **Fix year buttons first** (primary requirement)
2. **Add quarterly buttons** (secondary requirement)
3. **Combine year + quarter filtering** (advanced feature)

## Recommended Manual Fix Steps

1. **Check current button event listeners** in visual_mockup.html
2. **Verify data access patterns** for year filtering
3. **Test with console.log()** to track button clicks
4. **Update chart functions** to use selected year/quarter
5. **Add quarterly buttons** if year fix works
6. **Test combined filtering** (year + quarter)

## Success Criteria
- [ ] Year buttons filter data correctly
- [ ] Active button highlighting works
- [ ] Charts update smoothly on button clicks
- [ ] Quarterly buttons added and functional
- [ ] Combined year + quarter filtering works
