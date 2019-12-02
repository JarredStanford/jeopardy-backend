import json

jeopardy = open('../questions.json')
jeopardyQs = json.load(jeopardy)


Answer(category= question['category'], air_date = question['air_date'], question = question['question'], value = question['value'], answer = question['answer'], round = question['round'], show_number = question['show_number'])

        
