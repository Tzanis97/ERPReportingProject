-- Ποια πλοία έκαναν τα περισσότερα ταξίδια το 2024

SELECT 
    s.name AS ShipName,
    COUNT(v.voyage_id) AS VoyageCount
FROM Voyages v
JOIN Ships s ON v.ship_id = s.ship_id
WHERE YEAR(v.departure_date) = 2024
GROUP BY s.name
ORDER BY VoyageCount DESC;