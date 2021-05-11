#!/usr/bin/env python3

import csv
import datetime
from pprint import pprint


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output=None):
	result = []
	with open(source_log) as f:
		reader = csv.reader(f)
		log_list = []
		unique_emails = []
		profile = []
		for line in reader:
			if '@' in line[1]:
				log_list.append(line)
				if line[1] not in profile:
					unique_emails.append(line[1])
				profile.append(line[1])
			else:
				result.append(line)

		for email in unique_emails:
			logs_for_particular_mail = []
			for log in log_list:
				if log[1] == email:
					logs_for_particular_mail.append(log)

			dates_to_compare = []
			for log in logs_for_particular_mail:
				data_obj = convert_str_to_datetime(log[-1])
				log.append(data_obj)
				dates_to_compare.append(data_obj)
					
			for log in logs_for_particular_mail:			
				if max(dates_to_compare) in log:
					del log[-1]
					result.append(log) 
			
	with open(output, 'w') as r:
		writer = csv.writer(r)
		writer.writerows(result)


write_last_log_to_csv('mail_log.csv', '17_4_result.csv')
