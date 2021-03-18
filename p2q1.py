# <Your Team ID> G7_T20
# <Team members' names> Teo Eng Siang

# project 2 Q1

# replace the content of this function with your own algorithm
# inputs: 
#   p: min target no. of points player must collect. p>0
#   v: 1 (non-cycle) or 2 (cycle)
#   flags: 2D list [[flagID, value, x, y], [flagID, value, x, y]....]
# returns:
#   1D list of flagIDs to represent a route. e.g. [F002, F005, F003, F009]

def get_route(p, v, flags):
	flag_list = []
	sp_x = 0
	sp_y = 0
	total_score = 0

	while total_score < p :
		highest_weight = 0
		highest_flag_name = ""
		highest_flag_point = 0
		highest_dist = 1000000
		highest_x = 0.0
		highest_y = 0.0
		for flag in flags :
			if flag[0] in flag_list :
				continue
			points = int(flag[1])
			current_x = float(flag[2])
			current_y = float(flag[3])
			dist = ((sp_x - current_x)**2 + (sp_y - current_y)**2)**0.5
			if v == 1 :
				if dist < highest_dist:
					highest_dist = dist
					highest_flag_name = flag[0]
					highest_flag_point = points
					highest_x = current_x
					highest_y = current_y
			else :
				if total_score < (p * 0.75) :
					weight = points / dist
				else :
					dist_back_to_sp = ((0 - current_x)**2 + (0 - current_y)**2)**0.5
					dist = (dist + dist_back_to_sp)
					weight = points / dist

				if weight >= highest_weight and dist <= highest_dist:
					highest_weight = weight
					highest_flag_name = flag[0]
					highest_flag_point = points
					highest_x = current_x
					highest_y = current_y

		flag_list.append(highest_flag_name)
		total_score += highest_flag_point
		sp_x = highest_x
		sp_y = highest_y

	return flag_list