SELECT * FROM vpclog_utc9 WHERE (starttime BETWEEN timestamp '2021-07-01 00:00:00.000'AND timestamp '2021-07-03 23:59:59.000') 
and sourceaddress = '1.1.1.1' and (destinationaddress = '2.2.2.2' or destinationaddress = '3.3.3.3') ORDER BY  starttime;              
