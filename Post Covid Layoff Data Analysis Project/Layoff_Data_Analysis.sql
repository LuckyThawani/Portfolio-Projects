-- Exploratory Data Analysis --

-- Find out the details of the company where maximum number of people which were laid off in a single day

Select *
FROM Layoffs.layoffs
ORDER BY total_laid_off DESC
LIMIT 1;

-- Find out the details of the company where 100% of the population was laid off

SELECT * 
FROM Layoffs.layoffs
WHERE percentage_laid_off = 1;

-- Find out the overall number of employees laid off by the companies

Select company, SUM(total_laid_off)
FROM Layoffs.layoffs
GROUP BY company
ORDER BY 2 DESC;

-- Find out which industries were impacted the most

SELECT industry,SUM(total_laid_off)
FROM Layoffs.layoffs
GROUP BY industry
ORDER BY 2 DESC;

-- Find out which country was impacted the most

SELECT country,SUM(total_laid_off)
FROM Layoffs.layoffs
GROUP BY country
ORDER BY 2 DESC;

-- Find out total layoffs per year

SELECT YEAR('DATE'), SUM(total_laid_off)
FROM Layoffs.layoffs
GROUP BY YEAR('DATE')
ORDER BY 1;

-- Rolling Total of Layoffs Per Month

SELECT SUBSTRING(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM Layoffs.layoffs
GROUP BY dates
ORDER BY dates ASC;

-- Now use it in a CTE so we can query off of it

WITH DATE_CTE AS 
(
SELECT SUBSTRING(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM Layoffs.layoffs
GROUP BY dates
ORDER BY dates ASC
)
SELECT dates, SUM(total_laid_off) OVER (ORDER BY dates ASC) as rolling_total_layoffs
FROM DATE_CTE
ORDER BY dates ASC;


