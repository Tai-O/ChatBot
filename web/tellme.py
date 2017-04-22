# coding: utf-8
import sys
print sys.argv
import requests
import json

import urllib2
import urllib

url = 'http://localhost:5000'
bots_list = '/List'
wayne = '/WayneCramp'
lucien = '/LucienCramp'
tony = '/TonyParsens'
asklist = 'list'
start_session_with_wayne = 'start_session Wayne Cramp'
start_session_with_lucien = 'start_session Lucien Cramp'
start_session_with_tony = 'start_session Tony Parsens'
end_session = 'end_session'

def get_list():
	bots_url = url + bots_list
	ret = requests.get(bots_url)
	print ret.text

def contact_wayne():
	wayne_url = url + wayne
	ret = requests.get(wayne_url)
	print ret.text

def ask_wayne_questions(query):
	wayne_request = url + wayne + '/' + '<string:'+ query +'>'
	ret = requests.get(wayne_request)
	print 'Wayne: ' +  ret.text

def contact_lucien():
	lucien_url = url + lucien
	ret = requests.get(lucien_url)
	print ret.text

def ask_lucien_questions(query):
	lucien_request = url + lucien + '/' + '<string:'+ query +'>'
	ret = requests.get(lucien_request)
	print 'Lucien: ' + ret.text

def contact_tony():
	tony_url = url + tony
	ret = requests.get(tony_url)
	print ret.text

def ask_tony_questions(query):
	tony_request = url + tony + '/' + '<string:'+ query +'>'
	ret = requests.get(tony_request)
	print 'Tony: ' +  ret.text

def main():
	user_input = raw_input("How may I help you ? ask something: ")
	if asklist in user_input:
		response = get_list()
		if not response:
			user_input2 = raw_input()
			if start_session_with_wayne in user_input2:
				response_wayne = contact_wayne()
				if not response_wayne:
					wayne_input = raw_input()
					wayne_response = ask_wayne_questions(wayne_input)
					while True:
						ask_wayne_questions(raw_input())
						if 'end_session' in raw_input():
							print 'Session ended with Wayne'
							break
							sys.exit(0)
						elif start_session_with_lucien in raw_input():
							ask_lucien_questions(raw_input())
						elif start_session_with_tony in raw_input():
							ask_tony_questions(raw_input())
			elif start_session_with_lucien in user_input2:
				response_lucien = contact_lucien()
				if not response_lucien:
					lucien_input = raw_input()
					ask_lucien_questions(lucien_input)
					while True:
						ask_lucien_questions(raw_input())
						if end_session in raw_input():
							print 'Session ended with Lucien'
							break
							sys.exit(0)
						elif start_session_with_wayne in raw_input():
							ask_wayne_questions(raw_input())
						elif start_session_with_tony in raw_input():
							ask_tony_questions(raw_input())
			elif start_session_with_tony in user_input2:
				response_tony = contact_tony()
				if not response_tony:
					tony_input = raw_input()
					ask_tony_questions(tony_input)
					while True:
						ask_tony_questions(raw_input())
						if end_session in raw_input():
							print 'Session ended with Tony'
							break
							sys.exit(0)
						elif start_session_with_wayne in raw_input():
							ask_wayne_questions(raw_input())
						elif start_session_with_lucien in raw_input():
							ask_lucien_questions(raw_input())
	else:
		print("Sorry, not available. Please type ‘list’ to see available bots.")


if __name__== "__main__":
		main()