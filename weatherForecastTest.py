import unittest, weatherForecast
from subprocess import check_output

class WeatherForcecastTest(unittest.TestCase):
	
	def test_happy_path(self):
		actual_output = weatherForecast.forecast("Christchurch, NZ")
		expected_output = '''
Iteration 0
Textual date:   2017-04-14 06:00:00 GMT
Cloud cover:    76%
Humidity:       88%
Pressure:       998.94hPa
Temperature:    17.88degreesC
Wind direction: 348.511degrees
Wind speed:     6.93m/s

Iteration 1
Textual date:   2017-04-14 09:00:00 GMT
Cloud cover:    80%
Humidity:       88%
Pressure:       1000.08hPa
Temperature:    16.77degreesC
Wind direction: 0.00537109degrees
Wind speed:     6.17m/s

Iteration 2
Textual date:   2017-04-14 12:00:00 GMT
Cloud cover:    88%
Humidity:       88%
Pressure:       1000.09hPa
Temperature:    15.91degreesC
Wind direction: 355.002degrees
Wind speed:     6.11m/s

Iteration 3
Textual date:   2017-04-14 15:00:00 GMT
Cloud cover:    88%
Humidity:       88%
Pressure:       1000.2hPa
Temperature:    15degreesC
Wind direction: 340.5degrees
Wind speed:     5.21m/s

Iteration 4
Textual date:   2017-04-14 18:00:00 GMT
Cloud cover:    88%
Humidity:       92%
Pressure:       1000.17hPa
Temperature:    14.85degreesC
Wind direction: 354degrees
Wind speed:     4.36m/s

Iteration 5
Textual date:   2017-04-14 21:00:00 GMT
Cloud cover:    92%
Humidity:       92%
Pressure:       1001.19hPa
Temperature:    15.27degreesC
Wind direction: 11.001degrees
Wind speed:     4.73m/s

Iteration 6
Textual date:   2017-04-15 00:00:00 GMT
Cloud cover:    92%
Humidity:       90%
Pressure:       1001.91hPa
Temperature:    16.51degreesC
Wind direction: 348degrees
Wind speed:     4.11m/s

Iteration 7
Textual date:   2017-04-15 03:00:00 GMT
Cloud cover:    92%
Humidity:       88%
Pressure:       1002.21hPa
Temperature:    16.1degreesC
Wind direction: 297degrees
Wind speed:     5.16m/s

Iteration 8
Textual date:   2017-04-15 06:00:00 GMT
Cloud cover:    68%
Humidity:       97%
Pressure:       1005.02hPa
Temperature:    14.3degreesC
Wind direction: 251.002degrees
Wind speed:     3.87m/s

Iteration 9
Textual date:   2017-04-15 09:00:00 GMT
Cloud cover:    56%
Humidity:       100%
Pressure:       1008.25hPa
Temperature:    13.09degreesC
Wind direction: 254.504degrees
Wind speed:     2.18m/s

Iteration 10
Textual date:   2017-04-15 12:00:00 GMT
Cloud cover:    68%
Humidity:       100%
Pressure:       1010.81hPa
Temperature:    12.5degreesC
Wind direction: 201.002degrees
Wind speed:     1.87m/s

Iteration 11
Textual date:   2017-04-15 15:00:00 GMT
Cloud cover:    56%
Humidity:       100%
Pressure:       1012.85hPa
Temperature:    12.35degreesC
Wind direction: 112.001degrees
Wind speed:     1.87m/s

Iteration 12
Textual date:   2017-04-15 18:00:00 GMT
Cloud cover:    36%
Humidity:       100%
Pressure:       1014.75hPa
Temperature:    11.58degreesC
Wind direction: 31.502degrees
Wind speed:     1.41m/s

Iteration 13
Textual date:   2017-04-15 21:00:00 GMT
Cloud cover:    32%
Humidity:       100%
Pressure:       1017.57hPa
Temperature:    12.81degreesC
Wind direction: 299.006degrees
Wind speed:     2.07m/s

Iteration 14
Textual date:   2017-04-16 00:00:00 GMT
Cloud cover:    56%
Humidity:       100%
Pressure:       1019.29hPa
Temperature:    13.9degreesC
Wind direction: 233.512degrees
Wind speed:     2.31m/s

Iteration 15
Textual date:   2017-04-16 03:00:00 GMT
Cloud cover:    80%
Humidity:       100%
Pressure:       1019.64hPa
Temperature:    13.09degreesC
Wind direction: 200degrees
Wind speed:     3.37m/s

Iteration 16
Textual date:   2017-04-16 06:00:00 GMT
Cloud cover:    92%
Humidity:       100%
Pressure:       1020.63hPa
Temperature:    12.18degreesC
Wind direction: 189degrees
Wind speed:     2.51m/s

Iteration 17
Textual date:   2017-04-16 09:00:00 GMT
Cloud cover:    92%
Humidity:       100%
Pressure:       1021.35hPa
Temperature:    11.69degreesC
Wind direction: 165.003degrees
Wind speed:     1.53m/s

Iteration 18
Textual date:   2017-04-16 12:00:00 GMT
Cloud cover:    88%
Humidity:       100%
Pressure:       1021.12hPa
Temperature:    11.49degreesC
Wind direction: 111.501degrees
Wind speed:     1.07m/s

Iteration 19
Textual date:   2017-04-16 15:00:00 GMT
Cloud cover:    44%
Humidity:       100%
Pressure:       1020.49hPa
Temperature:    11.32degreesC
Wind direction: 47.0019degrees
Wind speed:     1.51m/s

Iteration 20
Textual date:   2017-04-16 18:00:00 GMT
Cloud cover:    32%
Humidity:       100%
Pressure:       1019.44hPa
Temperature:    10.12degreesC
Wind direction: 40.5021degrees
Wind speed:     1.81m/s

Iteration 21
Textual date:   2017-04-16 21:00:00 GMT
Cloud cover:    64%
Humidity:       100%
Pressure:       1019.22hPa
Temperature:    12.03degreesC
Wind direction: 27.0003degrees
Wind speed:     2.37m/s

Iteration 22
Textual date:   2017-04-17 00:00:00 GMT
Cloud cover:    0%
Humidity:       99%
Pressure:       1018.7hPa
Temperature:    14.19degreesC
Wind direction: 13.0005degrees
Wind speed:     3.36m/s

Iteration 23
Textual date:   2017-04-17 03:00:00 GMT
Cloud cover:    0%
Humidity:       93%
Pressure:       1018.24hPa
Temperature:    15.02degreesC
Wind direction: 13.5009degrees
Wind speed:     1.52m/s

Iteration 24
Textual date:   2017-04-17 06:00:00 GMT
Cloud cover:    0%
Humidity:       94%
Pressure:       1019.22hPa
Temperature:    13.55degreesC
Wind direction: 57.5038degrees
Wind speed:     1.51m/s

Iteration 25
Textual date:   2017-04-17 09:00:00 GMT
Cloud cover:    12%
Humidity:       100%
Pressure:       1021.75hPa
Temperature:    11.3degreesC
Wind direction: 163.002degrees
Wind speed:     1.61m/s

Iteration 26
Textual date:   2017-04-17 12:00:00 GMT
Cloud cover:    68%
Humidity:       100%
Pressure:       1024.39hPa
Temperature:    12.1degreesC
Wind direction: 178.002degrees
Wind speed:     5.37m/s

Iteration 27
Textual date:   2017-04-17 15:00:00 GMT
Cloud cover:    92%
Humidity:       100%
Pressure:       1026.22hPa
Temperature:    11.47degreesC
Wind direction: 194.5degrees
Wind speed:     4.36m/s

Iteration 28
Textual date:   2017-04-17 18:00:00 GMT
Cloud cover:    88%
Humidity:       100%
Pressure:       1027.58hPa
Temperature:    11.09degreesC
Wind direction: 213.501degrees
Wind speed:     3.87m/s

Iteration 29
Textual date:   2017-04-17 21:00:00 GMT
Cloud cover:    80%
Humidity:       100%
Pressure:       1029.54hPa
Temperature:    11.61degreesC
Wind direction: 210degrees
Wind speed:     3.87m/s

Iteration 30
Textual date:   2017-04-18 00:00:00 GMT
Cloud cover:    44%
Humidity:       100%
Pressure:       1030.24hPa
Temperature:    12.48degreesC
Wind direction: 199.002degrees
Wind speed:     2.68m/s

Iteration 31
Textual date:   2017-04-18 03:00:00 GMT
Cloud cover:    0%
Humidity:       99%
Pressure:       1029.5hPa
Temperature:    12.87degreesC
Wind direction: 170.501degrees
Wind speed:     1.79m/s

Iteration 32
Textual date:   2017-04-18 06:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1029.47hPa
Temperature:    11.44degreesC
Wind direction: 76.0019degrees
Wind speed:     1.41m/s

Iteration 33
Textual date:   2017-04-18 09:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1029.39hPa
Temperature:    10.05degreesC
Wind direction: 36.0106degrees
Wind speed:     3.21m/s

Iteration 34
Textual date:   2017-04-18 12:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1028.41hPa
Temperature:    10.55degreesC
Wind direction: 30.0007degrees
Wind speed:     4.88m/s

Iteration 35
Textual date:   2017-04-18 15:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1026.52hPa
Temperature:    11.24degreesC
Wind direction: 29.0005degrees
Wind speed:     4.57m/s

Iteration 36
Textual date:   2017-04-18 18:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1024.91hPa
Temperature:    10.3degreesC
Wind direction: 5.50217degrees
Wind speed:     2.27m/s

Iteration 37
Textual date:   2017-04-18 21:00:00 GMT
Cloud cover:    0%
Humidity:       100%
Pressure:       1024.72hPa
Temperature:    11degreesC
Wind direction: 283.501degrees
Wind speed:     1.7m/s
'''
		self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
	unittest.main()

