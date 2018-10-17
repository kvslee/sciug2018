expired_patron = '''SELECT
					p.record_num          AS "patron_record",
					max(n.last_name)      AS "last_name",
					max(n.first_name)     AS "first_name",
					to_char(p.expiration_date_gmt, 'YYYY/MM/DD') AS "expiration_date",
					count(c.id)           AS "checkout_count"
					FROM sierra_view.patron_view p
					JOIN sierra_view.patron_record_fullname n ON n.patron_record_id = p.id
					JOIN sierra_view.checkout c               ON c.patron_record_id = p.id
					WHERE 
					p.expiration_date_gmt < current_date
					GROUP BY 1,4
				ORDER BY 5 desc'''

expired_patron_home_library = '''SELECT
					p.record_num          AS "patron_record",
					max(n.last_name)      AS "last_name",
					max(n.first_name)     AS "first_name",
					to_char(p.expiration_date_gmt, 'YYYY/MM/DD') AS "expiration_date",
					count(c.id)           AS "checkout_count"
					FROM sierra_view.patron_view p
					JOIN sierra_view.patron_record_fullname n ON n.patron_record_id = p.id
					JOIN sierra_view.checkout c               ON c.patron_record_id = p.id
					WHERE 
					p.expiration_date_gmt < current_date AND
                    p.home_library_code = %(home_library)s
					GROUP BY 1,4
				ORDER BY 5 desc'''   

# Search for ILL Lending checkedout
ill_lending = '''SELECT pv.home_library_code, c.loanrule_code_num, 
				pa.region, pa.postal_code 
				FROM sierra_view.checkout AS c
				JOIN sierra_view.patron_view AS pv ON pv.id = c.patron_record_id
				JOIN sierra_view.patron_record_address AS pa ON pa.patron_record_id = c.patron_record_id
				WHERE NOW() - c.checkout_gmt <= interval '100 days' AND
				(c.loanrule_code_num = 93 OR c.loanrule_code_num = 15)
'''				             

ill_lending_home_library = '''SELECT pv.home_library_code, c.loanrule_code_num, 
				pa.region, pa.postal_code 
				FROM sierra_view.checkout AS c
				JOIN sierra_view.patron_view AS pv ON pv.id = c.patron_record_id
				JOIN sierra_view.patron_record_address AS pa ON pa.patron_record_id = c.patron_record_id
				WHERE NOW() - c.checkout_gmt <= interval '100 days' AND
				(c.loanrule_code_num = 93 OR c.loanrule_code_num = 15) AND
				pv.home_library_code = %(home_library)s
'''				             

ill_partners_home_library = '''SELECT pv.home_library_code, pv.record_num, pa.region, pa.postal_code 
							FROM sierra_view.patron_view as pv
							JOIN sierra_view.patron_record_address AS pa ON pa.patron_record_id = pv.id
							WHERE pv.ptype_code IN (22, 10)
							AND pv.home_library_code = %(home_library)s
							'''

ill_partners = '''SELECT pv.home_library_code, pv.record_num, pa.region, pa.postal_code 
					FROM sierra_view.patron_view as pv
					JOIN sierra_view.patron_record_address AS pa ON pa.patron_record_id = pv.id
					WHERE pv.ptype_code IN (22, 10)
					'''							