drop table TMP_Aplicacion_interactions;
create table TMP_Aplicacion_interactions as select tipo, fecha_interaccion , customer_id  from Aplicacion_interactions;
.mode csv
.import interactions.csv TMP_Aplicacion_interactions
insert into Aplicacion_interactions (tipo, fecha_interaccion , customer_id) select * from TMP_Aplicacion_interactions;
select 'Cantidad de customers:', count(*) from Aplicacion_interactions;
