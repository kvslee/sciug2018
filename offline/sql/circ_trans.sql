SELECT 
regexp_replace(ct.patron_home_library_code, '\s+$', '') AS patron_home_library_code, 
regexp_replace(ct.ptype_code, '\s+$', '') AS ptype_code, 
to_char(ct.transaction_gmt, 'YYYY/MM/DD') AS time, 
ct.op_code, 
ct.count_type_code_num, 
ct.application_name, 
ct.itype_code_num, 
regexp_replace(ct.item_location_code, '\s+$', '') AS item_location_code

FROM sierra_view.circ_trans AS ct
WHERE NOW() - ct.transaction_gmt <= interval %(interval)s AND ct.op_code IN %(trans_types)s