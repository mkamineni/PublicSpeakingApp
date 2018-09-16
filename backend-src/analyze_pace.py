

def process_response(response):
	parts=response["monologues"][0]["elements"]
	total_space_after_period, num_periods=0, 0
	total_space_after_comma, num_commas=0, 0 

	period, comma=False, False
	for ind in range(len(parts)):
		elem=parts[ind]
		if period:
			total_space_after_period+=end-elem["ts"]
			num_periods+=1
		elif comma:
			total_space_after_comma+=end-elem["ts"]
			num_commas+=1

		if "end_ts" in elem:
			end=elem["end_ts"]

		#reset the last value
		value=elem["value"]
		if value==".":
			period=True
		elif value==",":
			comma=True
		else:
			period, comma=False, False

	words_per_min=len(parts)/(end/60)

	pause_after_sent, pause_after_comma= None, None

	if num_periods:
		pause_after_sent=total_space_after_period/period_counter

	if num_commas:
		pause_after_comma=total_space_after_comma/num_commas

	return pause_after_sent, pause_after_comma, words_per_min, end