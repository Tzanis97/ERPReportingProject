-- Μέση διάρκεια ταξιδιού ανά πλοίο (σε μέρες)

SELECT 
    v.voyage_id,
    s.name AS ShipName,
    dp.name AS DeparturePort,
    ap.name AS ArrivalPort,
    v.departure_date,
    v.arrival_date,
    DATEDIFF(DAY, v.departure_date, v.arrival_date) AS DurationDays
FROM Voyages v
JOIN Ships s ON v.ship_id = s.ship_id
JOIN Ports dp ON v.departure_port_id = dp.port_id
JOIN Ports ap ON v.arrival_port_id = ap.port_id
ORDER BY v.departure_date;
