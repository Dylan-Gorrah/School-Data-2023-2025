#!/usr/bin/env python3
"""
School Performance Data Extractor
Extracts data from Excel files and creates developer-ready markdown documentation
"""

import pandas as pd
import os
import glob
from datetime import datetime

class SchoolDataExtractor:
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.school_name = "LOWRYVILLE INTERMEDIÊRE SKOOL"
        self.emis_no = "300023304"
        self.district = "PIXLEY-KA-SEME"
        self.province = "NORTHERN CAPE"
        
    def extract_summary_data(self):
        """Extract summary data from 2023 and 2024 files"""
        summary_data = {}
        
        # 2024 summary data
        try:
            df_2024 = pd.read_excel(os.path.join(self.data_directory, 'SUMMARY OF RESULTS GR R TO 9 2024.xls'))
            summary_data['2024'] = self._parse_summary_file(df_2024, '2024')
        except Exception as e:
            print(f"Error reading 2024 summary: {e}")
            
        # 2023 summary data
        try:
            df_2023 = pd.read_excel(os.path.join(self.data_directory, 'SUMMARY OF RESULTS GR R TOT 9 2023.xls'))
            summary_data['2023'] = self._parse_summary_file(df_2023, '2023')
        except Exception as e:
            print(f"Error reading 2023 summary: {e}")
            
        return summary_data
    
    def _parse_summary_file(self, df, year):
        """Parse summary file data"""
        data = {
            'quarters': {},
            'annual_summary': {}
        }
        
        # Find quarter sections
        current_quarter = None
        for i, row in df.iterrows():
            metric = str(row.iloc[0]).strip()
            
            if 'Quarter' in metric and current_quarter != metric:
                current_quarter = metric
                data['quarters'][current_quarter] = {}
                continue
                
            if current_quarter and 'Statistics per grade' in metric:
                # Next row should have grade headers
                if i + 1 < len(df):
                    headers = df.iloc[i + 1].tolist()[1:]  # Skip first column
                    # Extract grade data for next few rows
                    for j in range(i + 2, min(i + 8, len(df))):
                        if j < len(df):
                            row_metric = str(df.iloc[j].iloc[0]).strip()
                            if any(x in row_metric for x in ['Number of Learners', 'Percentage', 'Grade Average']):
                                values = df.iloc[j].tolist()[1:]  # Skip first column
                                data['quarters'][current_quarter][row_metric] = dict(zip(headers, values))
                break
        
        # Extract annual summary (last quarter data)
        if 'Quarter 4' in data['quarters'] or len(data['quarters']) > 0:
            last_quarter = list(data['quarters'].keys())[-1]
            data['annual_summary'] = data['quarters'][last_quarter]
            
        return data
    
    def extract_subject_data(self):
        """Extract subject-specific data by grade and year"""
        subject_data = {}
        
        # Get all subject files
        subject_files = glob.glob(os.path.join(self.data_directory, 'SUBJECT*.xls'))
        
        for file_path in subject_files:
            filename = os.path.basename(file_path)
            
            # Parse filename to get grade and year
            grade, year = self._parse_filename(filename)
            if not grade or not year:
                continue
                
            try:
                df = pd.read_excel(file_path)
                parsed_data = self._parse_subject_file(df, grade, year)
                
                if year not in subject_data:
                    subject_data[year] = {}
                subject_data[year][grade] = parsed_data
                
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
        return subject_data
    
    def _parse_filename(self, filename):
        """Parse grade and year from filename"""
        grade = None
        year = None
        
        # Extract grade
        if 'GR R' in filename:
            grade = 'R'
        elif 'GR 1' in filename:
            grade = '1'
        elif 'GR 2' in filename:
            grade = '2'
        elif 'GR 3' in filename:
            grade = '3'
        elif 'GR 4' in filename:
            grade = '4'
        elif 'GR 5' in filename:
            grade = '5'
        elif 'GR 6' in filename:
            grade = '6'
        elif 'GR 7' in filename:
            grade = '7'
        elif 'GR 8' in filename:
            grade = '8'
        elif 'GR 9' in filename:
            grade = '9'
            
        # Extract year
        if '2024' in filename:
            year = '2024'
        elif '2023' in filename:
            year = '2023'
            
        return grade, year
    
    def _parse_subject_file(self, df, grade, year):
        """Parse subject-specific file"""
        data = {
            'grade': grade,
            'year': year,
            'subjects': {},
            'achievement_levels': {}
        }
        
        # Find the header row with subjects
        header_row = None
        for i, row in df.iterrows():
            if 'Subject' in str(row.iloc[0]):
                header_row = i
                break
        
        if header_row is None:
            return data
            
        # Get achievement level definitions (usually 2 rows after header)
        level_row = header_row + 2
        if level_row < len(df):
            level_data = df.iloc[level_row].tolist()[2:]  # Skip Subject and % Average columns
            data['achievement_levels'] = {
                f'Level {i+1}': level for i, level in enumerate(level_data) if pd.notna(level)
            }
        
        # Extract subject data
        for i in range(header_row + 3, len(df)):
            row = df.iloc[i]
            subject = str(row.iloc[0]).strip()
            
            # Skip empty rows and headers
            if not subject or subject in ['nan', 'Grade', '<Grade>'] or 'Subject' in subject:
                continue
                
            # Extract subject metrics
            subject_data = {
                'average_mark': row.iloc[2] if len(row) > 2 and pd.notna(row.iloc[2]) else None,
                'achievement_distribution': {}
            }
            
            # Extract achievement level counts
            for j in range(3, min(len(row), len(data['achievement_levels']) + 3)):
                if pd.notna(row.iloc[j]):
                    level_key = f'Level {j-2}'
                    subject_data['achievement_distribution'][level_key] = int(row.iloc[j])
            
            data['subjects'][subject] = subject_data
            
        return data
    
    def generate_markdown_report(self, summary_data, subject_data):
        """Generate comprehensive markdown report"""
        md_content = []
        
        # Header
        md_content.append("# School Performance Data Report")
        md_content.append(f"**School:** {self.school_name}")
        md_content.append(f"**EMIS Number:** {self.emis_no}")
        md_content.append(f"**District:** {self.district}")
        md_content.append(f"**Province:** {self.province}")
        md_content.append(f"**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        md_content.append("")
        
        # Table of Contents
        md_content.append("## Table of Contents")
        md_content.append("- [Executive Summary](#executive-summary)")
        md_content.append("- [Enrollment Data](#enrollment-data)")
        md_content.append("- [Academic Performance](#academic-performance)")
        md_content.append("- [Subject Performance Analysis](#subject-performance-analysis)")
        md_content.append("- [Year-over-Year Comparisons](#year-over-year-comparisons)")
        md_content.append("- [Trends and Patterns](#trends-and-patterns)")
        md_content.append("- [Data Quality Notes](#data-quality-notes)")
        md_content.append("- [Developer Notes](#developer-notes)")
        md_content.append("")
        
        # Executive Summary
        md_content.append("## Executive Summary")
        md_content.append("")
        md_content.append("This report provides a comprehensive analysis of school performance data for Lowryville Intermediate School covering grades R-9 for the years 2023-2024.")
        md_content.append("")
        
        # Enrollment Data Section
        md_content.append("## Enrollment Data")
        md_content.append("")
        md_content.append("### Enrollment by Grade and Year")
        md_content.append("")
        md_content.append("| Grade | 2023 Enrollment | 2024 Enrollment | Change | % Change |")
        md_content.append("|-------|-----------------|-----------------|--------|----------|")
        
        # Extract enrollment data from summary
        enrollment_comparison = self._extract_enrollment_comparison(summary_data)
        for grade_data in enrollment_comparison:
            md_content.append(f"| {grade_data['grade']} | {grade_data.get('2023') or 'N/A'} | {grade_data.get('2024') or 'N/A'} | {grade_data.get('change') or 'N/A'} | {grade_data.get('percent_change') or 'N/A'} |")
        
        md_content.append("")
        md_content.append("**Data Type:** Count (Number of learners)")
        md_content.append("**Notes:** Enrollment numbers represent total learners per grade for the academic year.")
        md_content.append("")
        
        # Academic Performance Section
        md_content.append("## Academic Performance")
        md_content.append("")
        
        # Pass Rates
        md_content.append("### Pass Rates by Grade")
        md_content.append("")
        md_content.append("| Grade | 2023 Pass Rate | 2024 Pass Rate | Change | Trend |")
        md_content.append("|-------|----------------|----------------|--------|--------|")
        
        pass_rate_comparison = self._extract_pass_rate_comparison(summary_data)
        for grade_data in pass_rate_comparison:
            trend = self._calculate_trend(grade_data.get('2023'), grade_data.get('2024'))
            md_content.append(f"| {grade_data['grade']} | {grade_data.get('2023') or 'N/A'}% | {grade_data.get('2024') or 'N/A'}% | {grade_data.get('change') or 'N/A'}% | {trend} |")
        
        md_content.append("")
        md_content.append("**Data Type:** Percentage")
        md_content.append("**Notes:** Pass rates represent percentage of learners who achieved promotion/passing status.")
        md_content.append("")
        
        # Grade Averages
        md_content.append("### Grade Average Performance")
        md_content.append("")
        md_content.append("| Grade | 2023 Average | 2024 Average | Change | Performance Level |")
        md_content.append("|-------|--------------|--------------|--------|-------------------|")
        
        average_comparison = self._extract_average_comparison(summary_data)
        for grade_data in average_comparison:
            performance_level = self._categorize_performance(grade_data.get('2024'))
            md_content.append(f"| {grade_data['grade']} | {grade_data.get('2023') or 'N/A'}% | {grade_data.get('2024') or 'N/A'}% | {grade_data.get('change') or 'N/A'}% | {performance_level} |")
        
        md_content.append("")
        
        # Subject Performance Analysis
        md_content.append("## Subject Performance Analysis")
        md_content.append("")
        
        for year in sorted(subject_data.keys(), reverse=True):
            md_content.append(f"### {year} Subject Performance")
            md_content.append("")
            
            for grade in sorted(subject_data[year].keys()):
                grade_data = subject_data[year][grade]
                md_content.append(f"#### Grade {grade} - {year}")
                md_content.append("")
                md_content.append("| Subject | Average Mark | Performance Level | Achievement Distribution |")
                md_content.append("|---------|--------------|------------------|------------------------|")
                
                for subject, data in grade_data['subjects'].items():
                    if data['average_mark']:
                        perf_level = self._categorize_performance(data['average_mark'])
                        dist_summary = self._summarize_achievement_distribution(data['achievement_distribution'])
                        md_content.append(f"| {subject} | {data['average_mark']:.1f}% | {perf_level} | {dist_summary} |")
                
                md_content.append("")
        
        # Year-over-Year Comparisons
        md_content.append("## Year-over-Year Comparisons")
        md_content.append("")
        
        # Enrollment trends
        md_content.append("### Enrollment Trends")
        md_content.append("")
        total_2023 = sum([d.get('2023') for d in enrollment_comparison if d.get('2023')])
        total_2024 = sum([d.get('2024') for d in enrollment_comparison if d.get('2024')])
        total_change = total_2024 - total_2023 if total_2023 and total_2024 else None
        total_percent_change = (total_change / total_2023 * 100) if total_2023 and total_2024 and total_change else None
        
        md_content.append(f"- **Total Enrollment 2023:** {total_2023 or 'N/A'} learners")
        md_content.append(f"- **Total Enrollment 2024:** {total_2024 or 'N/A'} learners")
        md_content.append(f"- **Net Change:** {total_change or 'N/A'} learners ({total_percent_change or 'N/A'}%)")
        md_content.append("")
        
        # Performance trends
        md_content.append("### Performance Trends")
        md_content.append("")
        pass_2023_values = [d.get('2023') for d in pass_rate_comparison if d.get('2023')]
        pass_2024_values = [d.get('2024') for d in pass_rate_comparison if d.get('2024')]
        avg_pass_2023 = sum(pass_2023_values) / len(pass_2023_values) if pass_2023_values else 0
        avg_pass_2024 = sum(pass_2024_values) / len(pass_2024_values) if pass_2024_values else 0
        
        md_content.append(f"- **Average Pass Rate 2023:** {avg_pass_2023:.1f}%")
        md_content.append(f"- **Average Pass Rate 2024:** {avg_pass_2024:.1f}%")
        md_content.append(f"- **Pass Rate Change:** {avg_pass_2024 - avg_pass_2023:.1f}%")
        md_content.append("")
        
        # Trends and Patterns
        md_content.append("## Trends and Patterns")
        md_content.append("")
        md_content.append("### Key Findings")
        md_content.append("")
        
        # Analyze trends
        trends = self._analyze_trends(enrollment_comparison, pass_rate_comparison, average_comparison)
        for trend in trends:
            md_content.append(f"- {trend}")
        
        md_content.append("")
        
        # Data Quality Notes
        md_content.append("## Data Quality Notes")
        md_content.append("")
        md_content.append("### Missing Data Points")
        md_content.append("")
        
        missing_data = self._identify_missing_data(summary_data, subject_data)
        for item in missing_data:
            md_content.append(f"- {item}")
        
        md_content.append("")
        md_content.append("### Data Consistency")
        md_content.append("")
        md_content.append("- Data extracted from official Department of Education reports")
        md_content.append("- Some grade levels (10-12) show no data - likely not offered at this school")
        md_content.append("- Quarterly data shows some variations in reporting consistency")
        md_content.append("")
        
        # Developer Notes
        md_content.append("## Developer Notes")
        md_content.append("")
        md_content.append("### Data Structure")
        md_content.append("")
        md_content.append("```json")
        md_content.append("{")
        md_content.append('  "school_info": {')
        md_content.append(f'    "name": "{self.school_name}",')
        md_content.append(f'    "emis_no": "{self.emis_no}",')
        md_content.append(f'    "district": "{self.district}",')
        md_content.append(f'    "province": "{self.province}"')
        md_content.append("  },")
        md_content.append('  "data_periods": ["2023", "2024"],')
        md_content.append('  "grade_levels": ["R", "1", "2", "3", "4", "5", "6", "7", "8", "9"],')
        md_content.append('  "data_types": {')
        md_content.append('    "enrollment": "count",')
        md_content.append('    "pass_rates": "percentage",')
        md_content.append('    "grade_averages": "percentage",')
        md_content.append('    "subject_performance": "percentage_and_counts"')
        md_content.append("  }")
        md_content.append("}")
        md_content.append("```")
        md_content.append("")
        
        # Chart Suggestions
        md_content.append("### Recommended Chart Types")
        md_content.append("")
        md_content.append("#### Enrollment Data")
        md_content.append("- **Bar Chart:** Grade-by-grade enrollment comparison (2023 vs 2024)")
        md_content.append("- **Line Chart:** Enrollment trends over time by grade")
        md_content.append("- **Pie Chart:** Grade distribution for each year")
        md_content.append("")
        
        md_content.append("#### Academic Performance")
        md_content.append("- **Bar Chart:** Pass rates by grade and year")
        md_content.append("- **Line Chart:** Grade average performance trends")
        md_content.append("- **Heatmap:** Performance matrix (grades vs years)")
        md_content.append("")
        
        md_content.append("#### Subject Performance")
        md_content.append("- **Bar Chart:** Subject average marks by grade")
        md_content.append("- **Stacked Bar Chart:** Achievement level distribution by subject")
        md_content.append("- **Radar Chart:** Subject performance comparison")
        md_content.append("")
        
        # API Endpoints Suggestion
        md_content.append("### Suggested API Endpoints")
        md_content.append("")
        md_content.append("```")
        md_content.append("GET /api/school/enrollment?year=2024&grade=all")
        md_content.append("GET /api/school/performance?year=2024&grade=8")
        md_content.append("GET /api/school/subjects?year=2024&grade=8&subject=mathematics")
        md_content.append("GET /api/school/trends?metric=pass_rate&grades=all")
        md_content.append("```")
        md_content.append("")
        
        return "\n".join(md_content)
    
    def _extract_enrollment_comparison(self, summary_data):
        """Extract enrollment comparison data"""
        comparison = []
        grades = ['R', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for grade in grades:
            grade_key = f'Gr {grade}' if grade != 'R' else 'Gr R'
            data = {'grade': grade}
            
            # Extract 2023 data
            if '2023' in summary_data and 'annual_summary' in summary_data['2023']:
                annual_2023 = summary_data['2023']['annual_summary']
                if 'Number of Learners' in annual_2023:
                    data['2023'] = annual_2023['Number of Learners'].get(grade_key)
            
            # Extract 2024 data
            if '2024' in summary_data and 'annual_summary' in summary_data['2024']:
                annual_2024 = summary_data['2024']['annual_summary']
                if 'Number of Learners' in annual_2024:
                    data['2024'] = annual_2024['Number of Learners'].get(grade_key)
            
            # Calculate change
            if data.get('2023') and data.get('2024'):
                data['change'] = data['2024'] - data['2023']
                data['percent_change'] = (data['change'] / data['2023']) * 100
            
            comparison.append(data)
        
        return comparison
    
    def _extract_pass_rate_comparison(self, summary_data):
        """Extract pass rate comparison data"""
        comparison = []
        grades = ['R', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for grade in grades:
            grade_key = f'Gr {grade}' if grade != 'R' else 'Gr R'
            data = {'grade': grade}
            
            # Extract 2023 data
            if '2023' in summary_data and 'annual_summary' in summary_data['2023']:
                annual_2023 = summary_data['2023']['annual_summary']
                # Look for percentage achieved/promoted
                for metric in ['Percentage of Learners Promoted (Passed)', 'Percentage of Learners: Achieved']:
                    if metric in annual_2023:
                        data['2023'] = annual_2023[metric].get(grade_key)
                        break
            
            # Extract 2024 data
            if '2024' in summary_data and 'annual_summary' in summary_data['2024']:
                annual_2024 = summary_data['2024']['annual_summary']
                for metric in ['Percentage of Learners Promoted (Passed)', 'Percentage of Learners: Achieved']:
                    if metric in annual_2024:
                        data['2024'] = annual_2024[metric].get(grade_key)
                        break
            
            # Calculate change
            if data.get('2023') and data.get('2024'):
                data['change'] = data['2024'] - data['2023']
            
            comparison.append(data)
        
        return comparison
    
    def _extract_average_comparison(self, summary_data):
        """Extract grade average comparison data"""
        comparison = []
        grades = ['R', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for grade in grades:
            grade_key = f'Gr {grade}' if grade != 'R' else 'Gr R'
            data = {'grade': grade}
            
            # Extract 2023 data
            if '2023' in summary_data and 'annual_summary' in summary_data['2023']:
                annual_2023 = summary_data['2023']['annual_summary']
                if 'Grade Average %' in annual_2023:
                    data['2023'] = annual_2023['Grade Average %'].get(grade_key)
            
            # Extract 2024 data
            if '2024' in summary_data and 'annual_summary' in summary_data['2024']:
                annual_2024 = summary_data['2024']['annual_summary']
                if 'Grade Average %' in annual_2024:
                    data['2024'] = annual_2024['Grade Average %'].get(grade_key)
            
            # Calculate change
            if data.get('2023') and data.get('2024'):
                data['change'] = data['2024'] - data['2023']
            
            comparison.append(data)
        
        return comparison
    
    def _categorize_performance(self, percentage):
        """Categorize performance level based on percentage"""
        if percentage is None:
            return "No Data"
        if percentage >= 80:
            return "Excellent"
        elif percentage >= 70:
            return "Good"
        elif percentage >= 60:
            return "Satisfactory"
        elif percentage >= 50:
            return "Moderate"
        else:
            return "Needs Improvement"
    
    def _calculate_trend(self, old_value, new_value):
        """Calculate trend indicator"""
        if not old_value or not new_value:
            return "No Data"
        
        change = new_value - old_value
        if change > 5:
            return "📈 Improving"
        elif change > 0:
            return "↗️ Slightly Improving"
        elif change > -5:
            return "➡️ Stable"
        else:
            return "📉 Declining"
    
    def _summarize_achievement_distribution(self, distribution):
        """Summarize achievement distribution"""
        if not distribution:
            return "No Data"
        
        total = sum(distribution.values())
        if total == 0:
            return "No Data"
        
        # Find the level with most learners
        max_level = max(distribution.items(), key=lambda x: x[1])
        return f"Peak: {max_level[0]} ({max_level[1]} learners)"
    
    def _analyze_trends(self, enrollment, pass_rates, averages):
        """Analyze trends and patterns"""
        trends = []
        
        # Enrollment trends
        enrollment_changes = [d['change'] for d in enrollment if d.get('change')]
        if enrollment_changes:
            avg_change = sum(enrollment_changes) / len(enrollment_changes)
            if avg_change > 0:
                trends.append(f"Enrollment is growing with an average increase of {avg_change:.1f} learners per grade")
            elif avg_change < 0:
                trends.append(f"Enrollment is declining with an average decrease of {abs(avg_change):.1f} learners per grade")
            else:
                trends.append("Enrollment remains stable across grades")
        
        # Performance trends
        pass_changes = [d['change'] for d in pass_rates if d.get('change')]
        if pass_changes:
            avg_pass_change = sum(pass_changes) / len(pass_changes)
            if avg_pass_change > 5:
                trends.append(f"Pass rates are improving significantly with an average increase of {avg_pass_change:.1f}%")
            elif avg_pass_change > 0:
                trends.append(f"Pass rates show slight improvement with an average increase of {avg_pass_change:.1f}%")
            elif avg_pass_change < -5:
                trends.append(f"Pass rates are declining with an average decrease of {abs(avg_pass_change):.1f}%")
        
        # Identify best and worst performing grades
        valid_averages = [(d['grade'], d.get('2024')) for d in averages if d.get('2024')]
        if valid_averages:
            best_grade = max(valid_averages, key=lambda x: x[1])
            worst_grade = min(valid_averages, key=lambda x: x[1])
            trends.append(f"Best performing grade: Grade {best_grade[0]} ({best_grade[1]:.1f}% average)")
            trends.append(f"Grade needing most support: Grade {worst_grade[0]} ({worst_grade[1]:.1f}% average)")
        
        return trends
    
    def _identify_missing_data(self, summary_data, subject_data):
        """Identify missing data points"""
        missing = []
        
        # Check for missing grades in summary data
        if '2024' in summary_data:
            annual_2024 = summary_data['2024'].get('annual_summary', {})
            if 'Number of Learners' in annual_2024:
                for grade, value in annual_2024['Number of Learners'].items():
                    if pd.isna(value):
                        missing.append(f"2024 enrollment data missing for {grade}")
        
        if '2023' in summary_data:
            annual_2023 = summary_data['2023'].get('annual_summary', {})
            if 'Number of Learners' in annual_2023:
                for grade, value in annual_2023['Number of Learners'].items():
                    if pd.isna(value):
                        missing.append(f"2023 enrollment data missing for {grade}")
        
        # Check for missing subject data
        for year in ['2023', '2024']:
            if year not in subject_data:
                missing.append(f"No subject data available for {year}")
                continue
            
            grades = ['R', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for grade in grades:
                if grade not in subject_data[year]:
                    missing.append(f"No subject data for Grade {grade} in {year}")
        
        # Check for missing staff/infrastructure data
        missing.append("Staff numbers and breakdown data not found in provided files")
        missing.append("Infrastructure/resource needs data not found in provided files")
        missing.append("Systemic test results data not found in provided files")
        
        return missing


def main():
    """Main execution function"""
    data_directory = r"c:\Users\Dylan\Desktop\school data VIsualieation\Raw data"
    
    print("Starting school data extraction...")
    
    # Initialize extractor
    extractor = SchoolDataExtractor(data_directory)
    
    # Extract data
    print("Extracting summary data...")
    summary_data = extractor.extract_summary_data()
    
    print("Extracting subject data...")
    subject_data = extractor.extract_subject_data()
    
    print("Generating markdown report...")
    markdown_content = extractor.generate_markdown_report(summary_data, subject_data)
    
    # Save report
    output_file = os.path.join(os.path.dirname(data_directory), "school_performance_data.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"Report generated successfully: {output_file}")
    print("\nData extraction complete!")
    
    # Print summary statistics
    print(f"\nSummary Statistics:")
    print(f"- Years processed: {list(summary_data.keys())}")
    print(f"- Subject files processed: {sum(len(year_data) for year_data in subject_data.values())}")
    
    for year, year_data in subject_data.items():
        print(f"- {year}: {len(year_data)} grades with subject data")


if __name__ == "__main__":
    main()
