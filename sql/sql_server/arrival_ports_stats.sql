-- Ποια ήταν τα πιο συχνά λιμάνια άφιξης

SELECT 
    p.name AS ArrivalPort,
    COUNT(*) AS Arrivals
FROM Voyages v
JOIN Ports p ON v.arrival_port_id = p.port_id
GROUP BY p.name
ORDER BY Arrivals DESC;
