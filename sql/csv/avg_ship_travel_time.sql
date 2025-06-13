SELECT 
    v.voyage_id,
    s.name AS ShipName,
    dp.name AS DeparturePort,
    ap.name AS ArrivalPort,
    v.departure_date,
    v.arrival_date,
    (v.arrival_date - v.departure_date) AS DurationDays
FROM 'data/voyages_with_kpis.csv' v
JOIN 'data/ships.csv' s ON v.ship_id = s.ship_id
JOIN 'data/ports.csv' dp ON v.departure_port_id = dp.port_id
JOIN 'data/ports.csv' ap ON v.arrival_port_id = ap.port_id
ORDER BY v.departure_date;
