SELECT 
    s.name AS ShipName,
    p.country AS ArrivalCountry,
    SUM(v.total_revenue_usd) AS TotalRevenue
FROM 'data/voyages_with_kpis.csv' v
JOIN 'data/ports.csv' p
    ON v.arrival_port_id = p.port_id
JOIN 'data/ships.csv' s 
    ON v.ship_id = s.ship_id
GROUP BY s.name, p.country
ORDER BY TotalRevenue DESC;