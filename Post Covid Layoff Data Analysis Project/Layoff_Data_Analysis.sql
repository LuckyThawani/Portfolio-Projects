# Q1. Total layoffs by company:  Find total layoffs per company and sort descending.

SELECT
	company,
    SUM(total_laid_off) as total_layoffs

FROM Layoffs.layoffs
WHERE total_laid_off IS NOT NULL
GROUP BY company
ORDER BY total_layoffs DESC;

# Q2. Top 5 companies with highest layoffs: Return top 5 companies by total layoffs.

SELECT
	company,
    SUM(total_laid_off) as total_layoffs

FROM Layoffs.layoffs
WHERE total_laid_off IS NOT NULL
GROUP BY company
ORDER BY total_layoffs DESC
LIMIT 5;

# Q3. Layoffs trend over time (monthly) : Find total layoffs per month.

SELECT
    DATE_FORMAT(STR_TO_DATE(date, '%m/%d/%Y'), '%Y-%m') AS month,
    SUM(total_laid_off) AS total_layoffs
FROM Layoffs.layoffs
GROUP BY month
ORDER BY month;

#Q4. Industry-wise layoffs share : Calculate total layoffs per industry and % contribution.

SELECT
    industry,
    SUM(total_laid_off) AS total_layoffs,
    (SUM(total_laid_off)  / SUM(SUM(total_laid_off)) OVER () ) *100 AS pct_contribution
FROM Layoffs.layoffs
WHERE total_laid_off IS NOT NULL
GROUP BY industry
ORDER BY pct_contribution DESC;

#Q5. Companies with layoffs above industry average: Find companies whose layoffs are above the average layoffs of their industry.

SELECT *
FROM (
    SELECT
        company,
        industry,
        SUM(total_laid_off) AS total_layoffs,
        AVG(SUM(total_laid_off)) OVER (PARTITION BY industry) AS avg_industry_layoffs
    FROM Layoffs.layoffs
    WHERE total_laid_off IS NOT NULL
    GROUP BY company, industry
) t
WHERE total_layoffs > avg_industry_layoffs;

#Q6. Rank companies by layoffs within each country.

SELECT

	company,
    country,
    SUM(total_laid_off) AS total_layoffs,
    DENSE_RANK() OVER (PARTITION BY country ORDER BY SUM(total_laid_off) DESC) AS ranking
FROM Layoffs.layoffs
    WHERE total_laid_off IS NOT NULL
    GROUP BY company, country  
    
#Q7. Calculate cumulative layoffs by date OR over time (Running Total, to find out overall layoffs progression)

SELECT

	STR_TO_DATE(date, '%m/%d/%Y') AS date,
    SUM(total_laid_off) AS total_layoffs,
    SUM(SUM(total_laid_off)) OVER (
        ORDER BY STR_TO_DATE(date, '%m/%d/%Y')
    ) AS cumulative_layoffs
FROM Layoffs.layoffs
    WHERE total_laid_off IS NOT NULL
    GROUP BY date 
    
    
#Q8. Identify Layoff Spikes (Day-over-Day Increase). Find days where layoffs increased compared to previous day

SELECT *
FROM (
    SELECT
        date,
        total_layoffs,
        LAG(total_layoffs) OVER (ORDER BY date) AS prev_day_layoffs
    FROM (
        SELECT
            date,
            SUM(total_laid_off) AS total_layoffs
        FROM layoffs
        WHERE total_laid_off IS NOT NULL
        GROUP BY date
    ) t1
) t2
WHERE total_layoffs > prev_day_layoffs;

















