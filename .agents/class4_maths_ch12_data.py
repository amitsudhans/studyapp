# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 12: Ticking Clocks and Turning Calendar
Full 20-slide structured curriculum dataset.
"""

SLIDES_DATA = [   {   'checkpoints': [   {   'ans': 2,
                               'exp': 'A leap year has 366 days because February receives an extra 29th day.',
                               'options': ['364 days', '365 days', '366 days', '368 days'],
                               'q': 'How many days are there in a standard leap year?'},
                           {   'ans': 2,
                               'exp': '2024 is evenly divisible by 4 (2024 ÷ 4 = 506 with remainder 0), making it a '
                                      'leap year.',
                               'options': ['2022', '2023', '2024', '2025'],
                               'q': 'Which of the following years is a leap year?'}],
        'id': 1,
        'section': 'Solar Orbit & February Twenty-Ninth',
        'speech': 'Welcome to the fascinating study of time and calendars, where planetary motions dictate our daily '
                  'clocks and yearly seasons! Under our standard Gregorian solar calendar, an ordinary year contains '
                  'precisely three hundred sixty-five days. However, the Earth takes approximately three hundred '
                  'sixty-five days and six hours to complete one full revolution around the Sun. Because an ordinary '
                  'calendar counts only full days, those extra six hours accumulate silently year after year. Over '
                  'four consecutive years, four times six hours equals twenty-four extra hours, which creates exactly '
                  'one full additional day! To keep our calendar perfectly synchronized with the astronomical seasons, '
                  'this extra day is added to the shortest month of the year, February. While February normally has '
                  'twenty-eight days, during a leap year it gains an extra day, giving it twenty-nine days, and making '
                  'the entire year three hundred sixty-six days long! A child born on February twenty-ninth is '
                  'lovingly called a leapling, celebrating an official calendar birthday once every four years! Notice '
                  'that leap years are divisible by four: twenty-twenty, twenty-twenty-four, and twenty-twenty-eight '
                  'are all leap years. Regularly understanding leap years reveals how astronomers and mathematicians '
                  'harmonize human timekeeping with cosmic planetary cycles across generations.',
        'title': 'Leap Year Calendar'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'DD is 05 (fifth day), MM is 09 (ninth month, September), and YYYY is 2026.',
                               'options': ['May 9, 2026', '5 September 2026', '9 May 2026', '5 October 2026'],
                               'q': 'In the standard date format DD/MM/YYYY, what does the date 05/09/2026 represent?'},
                           {   'ans': 2,
                               'exp': '2024 - 2012 = 12 years.',
                               'options': ['10 years', '11 years', '12 years', '14 years'],
                               'q': 'If a person was born on 12/04/2012, how old will they be on 12/04/2024?'}],
        'id': 2,
        'section': 'Standard Notation & Calendar Intervals',
        'speech': 'Dates allow us to record historical milestones, schedule school events, and celebrate birthdays '
                  'with orderly precision. In India and many parts of the world, dates are officially written using '
                  'the day-month-year format, abbreviated as DD-MM-YYYY. In this layout, the first two digits '
                  'represent the calendar day, the middle two digits signify the month of the year, and the final four '
                  'digits denote the calendar year. For instance, the fifteenth of August nineteen forty-seven is '
                  'written as fifteen-zero-eight-nineteen-forty-seven. Translating between month numbers and names '
                  'requires remembering their calendar order: zero-one represents January, zero-two represents '
                  'February, and twelve represents December. Calculating age differences from birth dates is another '
                  'valuable mathematical skill. For example, if an energetic young learner was born on the tenth of '
                  'March twenty-fourteen, how old will that student be on the tenth of March twenty-twenty-four? '
                  'Because the day and month match, we simply subtract the birth year from the target year: '
                  'twenty-twenty-four minus twenty-fourteen equals exactly ten years of age! Regularly tracking '
                  'consecutive calendar days, yesterday, today, and tomorrow, reinforces cyclic modular arithmetic '
                  'base-seven, proving that standard date formatting transforms flowing chronological time into '
                  'organized, calculable mathematical records for civil society and school documentation.',
        'title': 'Date Formats Math'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '14 + 3 = 17, so the milk must be consumed by 17/07/2024.',
                               'options': ['15/07/2024', '16/07/2024', '17/07/2024', '20/07/2024'],
                               'q': 'If milk is packed on 14/07/2024 with a shelf life of 3 days, by what date must it '
                                    'be consumed?'},
                           {   'ans': 2,
                               'exp': 'Month 3 (March) + 6 months = Month 9 (September 2024).',
                               'options': ['July 2024', 'August 2024', 'September 2024', 'October 2024'],
                               'q': "A packet of biscuits manufactured in March 2024 states 'Best before 6 months'. "
                                    'Which is the last safe consumption month?'}],
        'id': 3,
        'section': 'Consumer Protection & Shelf Life Calculations',
        'speech': 'Whenever you visit a grocery store or bakery, inspecting package labels is an essential consumer '
                  'safety habit grounded in practical date arithmetic. Commercial food products, dairy cartons, '
                  'medicine bottles, and packaged snacks display two vital dates: the manufacturing date, abbreviated '
                  'as M-F-G, and the expiry or best-before date, often abbreviated as E-X-P. The manufacturing date '
                  'tells us precisely when the item was produced in the factory, while the expiry date indicates the '
                  'final date until which the product remains fresh, safe, and wholesome to consume. The duration '
                  'between these two critical dates is called the product shelf life. Suppose a box of wholesome '
                  'butter cookies displays a manufacturing date of zero-five-zero-one-twenty-twenty-four, and the '
                  'commercial package label clearly specifies best before six months from manufacture. When does this '
                  'product expire? Adding six full calendar months to January brings us to the fifth of July '
                  'twenty-twenty-four! If an alert customer inspects the package on the tenth of August, the cookies '
                  'are past their expiry date and should never be purchased. Carefully calculating product shelf life '
                  'in months and days protects public community health, effectively prevents accidental food waste, '
                  'and vividly illustrates how practical calendar math directly safeguards our everyday physical '
                  'wellbeing.',
        'title': 'Product Expiry Dates'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'A synodic lunar month lasts approximately 29.5 days.',
                               'options': ['7 days', '15 days', '29.5 days', '365 days'],
                               'q': 'How long does a complete lunar phase cycle (from one new moon to the next) last '
                                    'approximately?'},
                           {   'ans': 1,
                               'exp': 'Shukla Paksha is the bright waxing fortnight leading up to the full moon '
                                      '(Purnima).',
                               'options': ['Krishna Paksha', 'Shukla Paksha', 'Amavasya', 'Purnima'],
                               'q': 'In the Indian lunar calendar, what is the fortnight of the waxing (brightening) '
                                    'moon called?'}],
        'id': 4,
        'section': 'Cultural Astronomy & Lunar Month Cycles',
        'speech': 'While the solar Gregorian calendar governs international civic commerce, rich community calendars '
                  'celebrate cultural heritage and astronomical traditions across diverse civilizations. India has a '
                  'vibrant tradition of lunisolar calendars, such as the Saka and Vikram Samvat calendars, alongside '
                  'the Islamic Hijri calendar, the Sikh Nanakshahi calendar, and regional harvesting calendars. Unlike '
                  "solar calendars that track only the Earth's orbit around the Sun, lunar calendars track the "
                  'recurring phases of the Moon! A complete lunar cycle lasts approximately twenty-nine and a half '
                  'days, moving from the invisible new moon, called Amavasya, to the glowing full moon, called '
                  'Purnima. In traditional Indian calendars, each month is divided into two fortnights or pakshes of '
                  'fifteen lunar days each: Shukla Paksha, the waxing fortnight of growing moonlight, and Krishna '
                  'Paksha, the waning fortnight of fading light. Celebrated community festivals like Diwali, Eid, '
                  'Gurpurab, and Holi are all determined by these celestial lunar positions! Traditional calendars '
                  'also feature poetic month names like Chaitra, Vaisakha, Kartika, and Ramadan. Exploring community '
                  'calendars deepens our cultural appreciation, showing that time can be measured through changing '
                  'shadows of the Moon just as meaningfully as by the ticking hands of mechanical clocks everywhere in '
                  'daily life.',
        'title': 'Community Lunar Calendars'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'One full rotation of Earth on its axis takes exactly 24 hours.',
                               'options': ['12 hours', '18 hours', '24 hours', '30 hours'],
                               'q': 'How many total hours are there in one complete day and night cycle?'},
                           {   'ans': 1,
                               'exp': 'From 11 PM to midnight is 1 hour; from midnight to 6 AM is 6 hours. 1 + 6 = 7 '
                                      'hours.',
                               'options': ['6 hours', '7 hours', '8 hours', '9 hours'],
                               'q': 'If a doctor sleeps from 11:00 PM to 6:00 AM, how many hours of sleep did the '
                                    'doctor get?'}],
        'id': 5,
        'section': 'Daily Routine Cycles & Elapsed Durations',
        'speech': 'Have you ever wondered how many hours comprise one full natural day on Earth? One complete '
                  'planetary rotation of the Earth upon its axis takes exactly twenty-four hours! To visualize this '
                  'uninterrupted cycle, mathematicians and medical planners use a circular twenty-four-hour routine '
                  'wheel. Imagine a large wheel divided into twenty-four equal wedges, with each wedge representing '
                  "one sixty-minute hour. Let us examine a hospital doctor's busy daily routine plotted on this wheel. "
                  "The doctor sleeps soundly from eleven o'clock at night until six o'clock in the morning. Counting "
                  'the hourly sectors between eleven PM and six AM reveals exactly seven hours of restful sleep! '
                  'During the day, the doctor consults patients at the clinic from nine AM until one PM, which totals '
                  'four hours of medical service. Following lunch, hospital rounds continue from three PM to seven PM, '
                  'adding another four hours of healthcare work. The remaining hours are spent cooking fresh meals, '
                  'reading, exercising, and enjoying family conversation. Summing all the segments: seven hours '
                  'sleeping, eight hours working, and nine hours of meals and relaxation equals exactly twenty-four '
                  'hours! The twenty-four-hour wheel teaches us how to budget time wisely, balance responsibilities, '
                  'and calculate elapsed durations effortlessly.',
        'title': 'Daily Routine Wheel'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'AM stands for Ante Meridiem, meaning before midday (the period from midnight to '
                                      'noon).',
                               'options': [   'After Midnight',
                                              'Ante Meridiem (before midday)',
                                              'All Morning',
                                              'Annual Meeting'],
                               'q': "What does the Latin abbreviation 'AM' stand for in 12-hour time?"},
                           {   'ans': 1,
                               'exp': 'Evening hours following midday are designated with PM (Post Meridiem).',
                               'options': ['8:00 AM', '8:00 PM', '8:00 Noon', '8:00 Midnight'],
                               'q': "Which time notation correctly describes having dinner at 8 o'clock in the "
                                    'evening?'}],
        'id': 6,
        'section': 'Ante Meridiem & Post Meridiem Notation',
        'speech': 'Most standard analog wall clocks and household wristwatches feature a circular dial numbered '
                  'sequentially from one through twelve. Because a full day contains twenty-four hours, the short hour '
                  'hand must travel around the clock face twice every day! This creates an interesting ambiguity: when '
                  "a clock displays eight o'clock, is it time for morning school assembly, or time for evening "
                  'bedtime? To resolve this confusion, timekeepers use two Latin designations: AM and PM. AM stands '
                  'for Ante Meridiem, which translates to before midday, while PM stands for Post Meridiem, meaning '
                  'after midday! The critical dividing line occurs precisely at twelve noon, when the radiant Sun '
                  'reaches its highest point in the sky. Midnight, the moment the new calendar day begins, is '
                  'designated as twelve midnight or twelve AM. From twelve midnight until twelve noon, all times are '
                  'labeled AM: seven AM is breakfast time, and ten AM is morning class. At twelve noon, the label '
                  'shifts to PM. From twelve noon until midnight, times are labeled PM: five PM is playground '
                  'playtime, and eight PM is evening dinner! AM and PM notation ensures clear, unambiguous '
                  'communication across school timetables, television schedules, train timetables, flight rosters, and '
                  'everyday social appointments.',
        'title': 'Twelve Hour Clocks'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '8:00 PM + 12:00 = 20:00 hours.',
                               'options': ['08:00 hours', '18:00 hours', '20:00 hours', '22:00 hours'],
                               'q': 'How is 8:00 PM represented on a 24-hour digital railway clock?'},
                           {   'ans': 1,
                               'exp': '17:30 - 12:00 = 5:30 PM.',
                               'options': ['5:30 AM', '5:30 PM', '7:30 PM', '3:30 PM'],
                               'q': 'What 12-hour AM/PM time corresponds to 17:30 hours on a train ticket?'}],
        'id': 7,
        'section': 'Converting 12-Hour to 24-Hour Formats',
        'speech': 'While home wall clocks use twelve-hour AM and PM notation, global transportation networks, '
                  'airlines, railways, and military operations rely on the twenty-four-hour digital clock format to '
                  'eliminate any possibility of AM and PM confusion. In a standard twenty-four-hour digital clock, '
                  'each day starts officially at midnight as zero-zero-zero-zero hours, and counts continuously '
                  'upwards to twenty-three-fifty-nine! Morning times from one AM to twelve noon look almost identical '
                  'in both systems: seven AM is written as zero-seven-hundred hours, and eleven-thirty AM is written '
                  'as eleven-thirty hours. However, once the clock passes twelve noon, the hours do not reset back to '
                  'one! Instead, they continue counting upwards: one PM becomes thirteen-hundred hours, two PM becomes '
                  'fourteen-hundred hours, and eight PM becomes twenty-hundred hours! The universal rule for '
                  'converting any PM time to twenty-four-hour time is simple: just add twelve to the hour! For '
                  'example, six-fifteen PM plus twelve hours equals eighteen-fifteen hours on the digital display! '
                  'Conversely, to convert a twenty-four-hour time back to PM notation, simply subtract twelve hours: '
                  'twenty-one-thirty minus twelve equals nine-thirty PM! Mastering twenty-four-hour digital time '
                  'enables observant young scholars to read train tickets, airport departure boards, and international '
                  'broadcast schedules with absolute confidence and mathematical clarity.',
        'title': 'Digital Clock Formats'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': 'From 6:15 to 7:15 is 1 hour. From 7:15 to 7:40 is 25 minutes. Total = 1 hour 25 '
                                      'minutes.',
                               'options': [   '1 hour 15 minutes',
                                              '1 hour 25 minutes',
                                              '1 hour 35 minutes',
                                              '2 hours 05 minutes'],
                               'q': 'A delivery courier starts at 6:15 AM and finishes at 7:40 AM. How long did the '
                                    'delivery route take?'},
                           {   'ans': 1,
                               'exp': '10:30 AM to 12:30 PM is 2 hours; 12:30 PM to 1:15 PM is 45 minutes. Total = 2 '
                                      'hours 45 minutes.',
                               'options': [   '2 hours 15 minutes',
                                              '2 hours 45 minutes',
                                              '3 hours 15 minutes',
                                              '3 hours 45 minutes'],
                               'q': 'If a bus departs at 10:30 AM and arrives at 1:15 PM, what is the travel '
                                    'duration?'}],
        'id': 8,
        'section': 'Analog Clocks & Duration Subtraction',
        'speech': 'Calculating elapsed time, the exact duration that elapses between a starting moment and an ending '
                  'moment, is one of the most practical skills in elementary mathematics. Consider a diligent dairy '
                  'courier who starts delivering fresh milk packets to neighborhood homes at six-fifteen in the '
                  'morning. When the final crate is delivered and the courier returns to the depot, the analog clock '
                  'displays seven-forty AM. How long did the delivery route take? To calculate elapsed time on an '
                  'analog clock, we break the interval into manageable benchmark steps. From six-fifteen AM, advancing '
                  "forty-five minutes brings us to the friendly top of the hour: seven o'clock! From seven o'clock to "
                  'seven-forty AM is another forty minutes. Adding both chunks together: forty-five minutes plus forty '
                  'minutes equals eighty-five minutes! Because sixty minutes make one full hour, eighty-five minutes '
                  'is equal to one hour and twenty-five minutes! Alternatively, we can subtract the starting time from '
                  'the ending time: seven hours and forty minutes minus six hours and fifteen minutes yields one hour '
                  'and twenty-five minutes. Tracking analog clock hands and decomposing intervals into round-hour '
                  'benchmarks transforms elapsed time calculations into joyful mental agility across our daily '
                  'routines and chores.',
        'title': 'Elapsed Time Intervals'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '60 minutes ÷ 4 = 15 minutes.',
                               'options': ['10 minutes', '15 minutes', '20 minutes', '30 minutes'],
                               'q': 'How many minutes are in one-quarter (1/4) of an hour?'},
                           {   'ans': 2,
                               'exp': "'Quarter to 6' means 15 minutes before 6:00, which is 5:45.",
                               'options': ['5:15', '5:30', '5:45', '6:15'],
                               'q': "What time is represented by 'quarter to 6'?"}],
        'id': 9,
        'section': 'Circular Clock Sectors & Fractional Hours',
        'speech': 'Connecting traditional circular clock faces with geometric fractions reveals how circular geometry '
                  'naturally represents parts of an hour. A standard clock dial forms a complete circle of three '
                  'hundred sixty degrees, containing sixty individual minute tick marks. When the long minute hand '
                  'travels half-way around the dial from twelve down to six, it sweeps across exactly thirty minutes. '
                  'Because thirty minutes is half of sixty minutes, we call this duration half an hour, written as the '
                  'fraction one-half! If the minute hand travels one-quarter of the way around the dial from twelve to '
                  'three, it sweeps across fifteen minutes, which is one-quarter of an hour! When fifteen minutes have '
                  'passed after an hour, timekeepers say quarter past the hour, such as quarter past four for '
                  'four-fifteen. When the minute hand sweeps three-quarters of the circle from twelve to nine, it '
                  'covers forty-five minutes, representing three-quarters of an hour! Because only fifteen minutes '
                  'remain until the next hour, we say quarter to the upcoming hour, such as quarter to five for '
                  'four-forty-five! Clearly visualizing shaded sectors on clock dials reinforces fraction concepts, '
                  'proving that sixty-minute intervals partition smoothly into halves, quarters, and three-quarters '
                  'during our daily study schedules and routines.',
        'title': 'Fractions Of Time'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': 'Each clock number equals 5 minutes. 7 × 5 = 35 minutes.',
                               'options': ['7 minutes', '25 minutes', '35 minutes', '42 minutes'],
                               'q': 'When the long minute hand points to 7 on the clock face, how many minutes have '
                                    'passed?'},
                           {   'ans': 1,
                               'exp': 'The hour hand has not reached 5 yet; it is 10 minutes before 5, which is 4:50.',
                               'options': ['5:50', '4:50', '4:10', '5:10'],
                               'q': 'If the hour hand is between 4 and 5 (close to 5) and the minute hand points to '
                                    '10, what time is it?'}],
        'id': 10,
        'section': 'Hand Discrimination & Diagnostic Analysis',
        'speech': 'Learning to read an analog clock accurately requires careful visual discrimination between the '
                  'short hour hand and the long minute hand. Beginner timekeepers often make common diagnostic errors '
                  'that teachers love to explore and clarify. The most frequent mistake happens when a student reads '
                  'the minute hand as if it were an hour hand! For example, when the minute hand points directly at '
                  'the numeral seven, an untrained student might mistakenly announce that it is seven minutes. But '
                  'each number on the clock dial represents a five-minute jump! Counting by fives: seven times five '
                  'equals thirty-five minutes! Another tricky trap occurs when reading the hour hand as it approaches '
                  'the next number. At eight-fifty, the minute hand points to ten, and the hour hand has crept very '
                  'close to the nine. Looking quickly, an inattentive observer might incorrectly call the time '
                  'nine-fifty! But because the minute hand has not yet reached twelve, the hour is still eight, making '
                  'the correct time eight-fifty! Recognizing that the short hand measures completed hours while the '
                  'long hand counts elapsed five-minute steps prevents common reading blunders, instilling lasting '
                  'precision and confidence whenever reading traditional ticking wall clocks at school.',
        'title': 'Clock Reading Errors'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '45 min + 45 min = 90 min = 1 hour 30 minutes.',
                               'options': [   '1 hour 15 minutes',
                                              '1 hour 30 minutes',
                                              '1 hour 45 minutes',
                                              '2 hours 00 minutes'],
                               'q': 'A student does math homework for 45 minutes and reads for 45 minutes. What is the '
                                    'total study time?'},
                           {   'ans': 2,
                               'exp': '4:20 PM to 5:20 PM is 1 hour; 5:20 PM to 5:50 PM is 30 minutes. Total = 1 hour '
                                      '30 minutes.',
                               'options': [   '1 hour 10 minutes',
                                              '1 hour 20 minutes',
                                              '1 hour 30 minutes',
                                              '1 hour 40 minutes'],
                               'q': 'If soccer practice begins at 4:20 PM and ends at 5:50 PM, how long did the '
                                    'practice last?'}],
        'id': 11,
        'section': 'Study Schedules & Activity Log Intervals',
        'speech': 'Managing daily study timetables, athletic sports practice sessions, and creative recreational '
                  'hobbies requires tracking how long activities last across our busy afternoons. For example, suppose '
                  'an organized fourth-grade student sits down to complete mathematics homework at five-fifteen PM. '
                  "The student works with steady concentration until six o'clock PM, and then switches immediately to "
                  'reading an adventure storybook until six-forty-five PM. How much total time did this diligent '
                  'student spend studying altogether? Let us break the session into two distinct chronological '
                  "intervals. First, from five-fifteen PM to six o'clock PM is exactly forty-five minutes of "
                  "mathematics problem-solving. Next, from six o'clock PM to six-forty-five PM is another dedicated "
                  'forty-five minutes of literature reading. Adding both individual durations together: forty-five '
                  'minutes plus forty-five minutes equals ninety minutes! Since sixty minutes constitute one full '
                  'hour, ninety minutes can be expressed as one hour and thirty minutes, or one and a half hours! '
                  'Keeping an active daily time log encourages responsible time budgeting, helping young learners '
                  'balance school assignments with outdoor playground games, evening household chores, and restful '
                  'sleep. Regularly practicing duration tracking strengthens mental addition, builds self-discipline, '
                  'and proves that every minute invested in focused learning yields rewarding intellectual growth and '
                  'life skills.',
        'title': 'Time Duration Tracking'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '24:00 - 20:15 = 3 hours 45 minutes.',
                               'options': [   '3 hours 15 minutes',
                                              '3 hours 45 minutes',
                                              '4 hours 15 minutes',
                                              '4 hours 45 minutes'],
                               'q': 'A train departs at 20:15 (8:15 PM) and arrives at midnight (24:00). How long was '
                                    'this first segment?'},
                           {   'ans': 2,
                               'exp': '3h 45m + 8h 45m = 11h 90m = 12 hours 30 minutes.',
                               'options': [   '11 hours 30 minutes',
                                              '12 hours 00 minutes',
                                              '12 hours 30 minutes',
                                              '13 hours 15 minutes'],
                               'q': 'An overnight train travels 3 hours 45 minutes before midnight and 8 hours 45 '
                                    'minutes after midnight. What is the total duration?'}],
        'id': 12,
        'section': 'Midnight Crossing & Long-Distance Journeys',
        'speech': 'Indian Railways operates one of the largest passenger train networks in the world, running '
                  'thousands of express trains day and night across our vast subcontinent. To ensure flawless '
                  'operational coordination across multiple states, railway timetables exclusively use the '
                  'twenty-four-hour system. Many popular express trains embark on overnight journeys that cross '
                  'midnight, introducing an exciting mathematical duration puzzle! Suppose the famous Rajdhani Express '
                  'departs from New Delhi railway station at twenty-hundred-fifteen hours, which corresponds to '
                  'eight-fifteen PM in the evening. The train arrives at its destination station the following morning '
                  'at zero-eight-forty-five hours, or eight-forty-five AM. How long was the entire overnight journey? '
                  'To solve this, we split the calculation at midnight, which is twenty-four-hundred hours. From '
                  'twenty-hundred-fifteen hours to midnight is three hours and forty-five minutes. From midnight to '
                  'zero-eight-forty-five hours the next morning is eight hours and forty-five minutes. Adding these '
                  'two segments: three hours plus eight hours equals eleven hours, while forty-five minutes plus '
                  'forty-five minutes equals ninety minutes! Regrouping sixty minutes as one hour gives twelve hours '
                  'and thirty minutes! Railway schedule arithmetic connects classroom time measurement with '
                  'cross-country travel, illustrating how twenty-four-hour clocks keep millions of passengers moving '
                  'safely and punctually every single day.',
        'title': 'Railway Time Schedules'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '15/11/2023 + 12 months = 15/11/2024; + 6 months = 15/05/2025.',
                               'options': ['15/05/2024', '15/11/2024', '15/05/2025', '15/11/2025'],
                               'q': 'A food product manufactured on 15/11/2023 has a shelf life of 18 months. What is '
                                    'its expiry date?'},
                           {   'ans': 1,
                               'exp': '9 - 2 = 7 days (1 week).',
                               'options': ['5 days', '7 days', '10 days', '14 days'],
                               'q': 'If yoghurt made on 02/09/2024 has an expiry date of 09/09/2024, what is its shelf '
                                    'life?'}],
        'id': 13,
        'section': 'Commercial Label Audits & Quality Control',
        'speech': 'Professional food inspectors, store accountants, and conscientious shoppers conduct careful shelf '
                  'life audits on packaged goods to ensure that families consume only fresh, safe, and wholesome '
                  'groceries. Let us examine how calendar arithmetic verifies product safety across various common '
                  'household food items. Consider a carton of fresh pasteurized milk with a manufacturing date of '
                  'twelve-zero-eight-twenty-twenty-four and a declared shelf life of four days. Simply adding four '
                  'days to the twelfth gives sixteen-zero-eight-twenty-twenty-four as the official final expiry date. '
                  'Next, consider a sealed tin of nutritious baby cereal manufactured on '
                  'twenty-five-zero-three-twenty-twenty-four, bearing a clear best-before label of twelve months. '
                  'Adding twelve full calendar months advances the year by one, setting the expiry date at '
                  'twenty-five-zero-three-twenty-twenty-five! Furthermore, what if an antiseptic medical ointment tube '
                  'is manufactured on fifteen-eleven-twenty-twenty-three with a verified shelf life of eighteen '
                  'months? Twelve months brings us to fifteen November twenty-twenty-four, and the remaining six '
                  'months advance the date to fifteen May twenty-twenty-five! If an observant store clerk discovers an '
                  'expired product on display shelves, it must be removed immediately without delay. Regularly '
                  'practicing commercial shelf life audits reinforces multi-month addition, leap year awareness, and '
                  'real-world consumer safety vigilance across local neighborhood markets, supermarkets, and grocery '
                  'stores.',
        'title': 'Shelf Life Inspection'},
    {   'checkpoints': [   {   'ans': 1,
                               'exp': '17 - 3 = 14 days, which is exactly 2 full weeks (2 × 7 = 14). So it is also '
                                      'Wednesday.',
                               'options': ['Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                               'q': 'If the 3rd of a month is a Wednesday, what day of the week will the 17th of the '
                                    'same month be?'},
                           {   'ans': 2,
                               'exp': '365 ÷ 7 = 52 weeks with a remainder of 1 day (52 × 7 = 364; 364 + 1 = 365).',
                               'options': [   '50 weeks and 5 days',
                                              '51 weeks and 2 days',
                                              '52 weeks and 1 day',
                                              '52 weeks and 2 days'],
                               'q': 'How many full weeks and leftover days are in an ordinary year of 365 days?'}],
        'id': 14,
        'section': 'Modular Seven Calendar Sequences & Cycles',
        'speech': 'The calendar week is an ancient, unbroken seven-day cycle that governs school timetables, public '
                  'holidays, and weekend rest periods. The seven days of the week, Monday, Tuesday, Wednesday, '
                  'Thursday, Friday, Saturday, and Sunday, repeat endlessly in predictable succession. Because a week '
                  'contains exactly seven days, any future date that is an exact multiple of seven days away will fall '
                  'on the exact same day of the week! For instance, if the third day of October is a Wednesday, adding '
                  'seven days tells us that the tenth of October must also be a Wednesday! Adding another seven days '
                  'reveals that the seventeenth and twenty-fourth of October are Wednesdays as well. This cyclic '
                  'property is based on modular arithmetic base-seven. How many weeks and days are in an ordinary '
                  'month of thirty-one days? Dividing thirty-one by seven yields four weeks with three days remaining, '
                  'since four times seven equals twenty-eight, and twenty-eight plus three equals thirty-one! In an '
                  'ordinary year of three hundred sixty-five days, dividing by seven reveals fifty-two full weeks plus '
                  'one odd day! This is why ordinary years begin and end on the exact same day of the week, '
                  'demonstrating the elegant mathematical structure linking days, weeks, and calendar cycles.',
        'title': 'Days And Weeks'},
    {   'checkpoints': [   {   'ans': 3,
                               'exp': '2000 ÷ 400 = 5 with remainder 0, so 2000 was a leap year.',
                               'options': ['1700', '1800', '1900', '2000'],
                               'q': 'According to the century leap rule, which of the following century years was a '
                                    'leap year?'},
                           {   'ans': 1,
                               'exp': '2100 ÷ 400 = 5 with remainder 100, so 2100 will be an ordinary year with 28 '
                                      'days in February.',
                               'options': [   'Yes, because it is divisible by 4',
                                              'No, because century years must be divisible by 400, and 2100 is not',
                                              'Yes, because all century years are leap years',
                                              'Cannot be determined'],
                               'q': 'Will the upcoming century year 2100 be a leap year?'}],
        'id': 15,
        'section': 'Solar Calibration & Four-Hundred Year Cycles',
        'speech': 'While most students know that leap years occur every four years, advanced calendar mathematics '
                  "includes an ingenious fine-tuning rule created by sixteenth-century astronomers. If the Earth's "
                  'orbit took exactly three hundred sixty-five days and six hours, adding one leap day every four '
                  'years would be completely perfect. But precise astronomical measurements reveal that Earth actually '
                  'takes three hundred sixty-five days, five hours, forty-eight minutes, and forty-five seconds to '
                  'orbit the Sun. That is about eleven minutes less than six hours! Adding a leap day every four years '
                  'slightly overcompensates, adding about three extra days every four hundred years! To correct this '
                  'subtle error, the Gregorian calendar introduced the century leap year rule: century years ending in '
                  'double zeros are leap years only if they are divisible by four hundred! Under this rule, the '
                  'century year sixteen hundred was a leap year, and the year two thousand was a leap year because two '
                  'thousand is divisible by four hundred. However, the century years seventeen hundred, eighteen '
                  'hundred, and nineteen hundred were ordinary years, and twenty-one hundred will not be a leap year! '
                  'This brilliant mathematical adjustment keeps our calendar accurate to within one day every three '
                  'thousand years.',
        'title': 'Century Leap Rules'},
    {   'checkpoints': [   {   'ans': 2,
                               'exp': '45m + 35m = 80m = 1h 20m. 2h + 3h + 1h = 6 hours 20 minutes.',
                               'options': [   '5 hours 80 minutes',
                                              '6 hours 10 minutes',
                                              '6 hours 20 minutes',
                                              '6 hours 30 minutes'],
                               'q': 'What is the sum of 2 hours 45 minutes and 3 hours 35 minutes?'},
                           {   'ans': 2,
                               'exp': '1 hour equals 60 minutes in base-60 time arithmetic.',
                               'options': ['10 minutes', '50 minutes', '60 minutes', '100 minutes'],
                               'q': 'In subtracting time, when you borrow 1 hour into the minutes column, how many '
                                    'minutes do you add?'}],
        'id': 16,
        'section': 'Base-Sixty Regrouping & Minute Borrowing',
        'speech': 'Adding and subtracting time requires mastering a unique mathematical base called the sexagesimal '
                  'system, or base-sixty arithmetic, inherited from ancient Babylonian astronomers. Unlike our '
                  'standard base-ten decimal system where we bundle ten units into one ten and ten tens into one '
                  'hundred, time arithmetic bundles sixty seconds into one minute, and sixty minutes into one hour! '
                  'Suppose we must add two hours and forty-five minutes to three hours and thirty-five minutes. Adding '
                  'the minutes first: forty-five plus thirty-five equals eighty minutes. Because eighty exceeds sixty, '
                  'we unbundle sixty minutes into one full hour, leaving twenty minutes behind! Adding the hours: two '
                  'plus three plus our carried one hour equals six hours, giving a total of six hours and twenty '
                  'minutes! Subtraction requires the inverse regrouping. Suppose we subtract one hour and fifty '
                  'minutes from four hours and twenty minutes. Because we cannot subtract fifty minutes from twenty '
                  'minutes, we borrow one hour from the four hours, leaving three hours. When that borrowed hour '
                  'enters the minute column, it transforms into sixty minutes! Adding sixty to twenty gives eighty '
                  'minutes, and eighty minus fifty leaves thirty minutes! Base-sixty arithmetic provides the universal '
                  'foundation for global navigation, astronomical calculations, and everyday timekeeping.',
        'title': 'Time Arithmetic Logic'},
    {   'id': 17,
        'quizzes': [   {   'ans': 2,
                           'exp': 'An ordinary year has 365 days, while a leap year has 366 days.',
                           'hint': 'February has 28 days in an ordinary year.',
                           'options': ['360 days', '364 days', '365 days', '366 days'],
                           'q': 'How many days does an ordinary non-leap year contain?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The Earth "
                                  "takes about 365 days and 6 hours to orbit the Sun.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>An ordinary calendar year rounds this to 365 full "
                                  "days.</li><li class='mb-2 text-slate-700 leading-relaxed'>The remaining 6 hours are "
                                  'accumulated over four years to form a leap year.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Ordinary years have "
                                  '365 days; leap years have 366 days.</div></div>'},
                       {   'ans': 1,
                           'exp': '4 years × 6 hours = 24 hours = 1 extra calendar day added to February.',
                           'hint': "Earth's orbit takes 365 days plus 6 extra hours each year.",
                           'options': [   'To match the 4 seasons',
                                          'Because 4 extra six-hour periods accumulate into 1 full 24-hour day',
                                          'Because clocks have 4 quadrants',
                                          'By royal decree'],
                           'q': 'Why does a leap year occur every 4 years in our calendar system?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Each solar "
                                  "year has an excess of approximately 6 hours over 365 days.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Over 4 years: 4 × 6 hours = 24 hours.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>24 hours equals exactly 1 full "
                                  "day.</li><li class='mb-2 text-slate-700 leading-relaxed'>This day is added to "
                                  "February as February 29th.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Four 6-hour orbital surpluses "
                                  'combine into one full leap day.</div></div>'},
                       {   'ans': 2,
                           'exp': '2024 ÷ 4 = 506 remainder 0. 2024 is a leap year.',
                           'hint': 'Check which year is evenly divisible by 4.',
                           'options': ['2018', '2021', '2024', '2026'],
                           'q': 'Which of the following years is a leap year?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>To determine "
                                  "if a year is a leap year, check divisibility by 4.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>2018 ÷ 4 = 504 remainder 2 (not a leap "
                                  "year).</li><li class='mb-2 text-slate-700 leading-relaxed'>2021 ÷ 4 = 505 remainder "
                                  "1 (not a leap year).</li><li class='mb-2 text-slate-700 leading-relaxed'>2024 ÷ 4 = "
                                  "506 remainder 0 (leap year!).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>2026 ÷ 4 = 506 remainder 2 (not a leap year).</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Years divisible by 4 "
                                  '(except non-400 century years) are leap years.</div></div>'},
                       {   'ans': 3,
                           'exp': '2020 + 4 = 2024, the next leap year.',
                           'hint': 'February 29 only appears in leap years, which occur every 4 years.',
                           'options': ['2021', '2022', '2023', '2024'],
                           'q': 'A child is born on February 29, 2020. In which year will the child celebrate their '
                                'next official calendar birthday?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>February 29 "
                                  "occurs exclusively in leap years.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Leap years occur every 4 years.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>2020 was a leap year; the next leap year is 2020 + 4 = "
                                  "2024.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Leapling birthdays on February 29 occur once every four years.</div></div>'},
                       {   'ans': 2,
                           'exp': 'Month number 11 corresponds to November.',
                           'hint': 'Look at the middle number MM in DD/MM/YYYY.',
                           'options': ['January', 'September', 'November', 'December'],
                           'q': 'In the standard date format DD/MM/YYYY, what month is indicated by 14/11/2025?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In DD/MM/YYYY, "
                                  "MM represents the two-digit month number.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Here, MM is 11.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The 11th month of the Gregorian calendar is "
                                  "November.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Month numbers 01 to 12 correspond sequentially from January to '
                                  'December.</div></div>'},
                       {   'ans': 0,
                           'exp': '15/08/1947 translates to 15 August 1947.',
                           'hint': 'DD is 15, MM is 08 (August), YYYY is 1947.',
                           'options': [   '15 August 1947 (Indian Independence Day)',
                                          '8 November 1947',
                                          '15 October 1947',
                                          '1 January 1947'],
                           'q': 'If an official government document is dated 15/08/1947, what historic event does it '
                                'mark in words?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>DD = 15 "
                                  "(fifteenth day).</li><li class='mb-2 text-slate-700 leading-relaxed'>MM = 08 "
                                  "(eighth month, August).</li><li class='mb-2 text-slate-700 leading-relaxed'>YYYY = "
                                  "1947.</li><li class='mb-2 text-slate-700 leading-relaxed'>In words, this is 15 "
                                  "August 1947, India's Independence Day.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Standard DD/MM/YYYY records day, "
                                  'month, and year with clarity.</div></div>'},
                       {   'ans': 2,
                           'exp': '2026 - 2014 = 12 years old.',
                           'hint': 'Subtract the birth year from the target year when day and month match.',
                           'options': ['10 years old', '11 years old', '12 years old', '14 years old'],
                           'q': 'A student was born on 20/06/2014. How old will this student be on 20/06/2026?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Both dates "
                                  "share the exact same day and month: 20 June.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Birth year = 2014; Target year = 2026.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Age = 2026 - 2014 = 12 years.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Subtract birth year "
                                  'from target year when day and month are identical.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Monday comes directly before Tuesday.',
                           'hint': 'Yesterday is the day immediately preceding today.',
                           'options': ['Sunday', 'Monday', 'Wednesday', 'Thursday'],
                           'q': 'If today is Tuesday, what day of the week was yesterday?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The days of "
                                  'the week in order are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, '
                                  "Saturday.</li><li class='mb-2 text-slate-700 leading-relaxed'>Yesterday means 1 day "
                                  "in the past.</li><li class='mb-2 text-slate-700 leading-relaxed'>One day before "
                                  "Tuesday is Monday.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Yesterday represents the previous "
                                  'day in the 7-day calendar cycle.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Friday + 1 day = Saturday (tomorrow); + 2 days = Sunday.',
                           'hint': 'Tomorrow is Saturday; the day after tomorrow is +2 days.',
                           'options': ['Saturday', 'Sunday', 'Monday', 'Tuesday'],
                           'q': 'If today is Friday, what day of the week will it be the day after tomorrow?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Today is "
                                  "Friday.</li><li class='mb-2 text-slate-700 leading-relaxed'>Tomorrow is Saturday "
                                  "(+1 day).</li><li class='mb-2 text-slate-700 leading-relaxed'>The day after "
                                  "tomorrow is Sunday (+2 days).</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> The day after tomorrow represents +2 "
                                  'days from the present day.</div></div>'},
                       {   'ans': 1,
                           'exp': 'February has 29 days in a leap year and 28 days in an ordinary year.',
                           'hint': 'February receives one additional day during a leap year.',
                           'options': ['28 days', '29 days', '30 days', '31 days'],
                           'q': 'How many days are in the month of February during a leap year?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In an ordinary "
                                  "year, February has 28 days.</li><li class='mb-2 text-slate-700 leading-relaxed'>In "
                                  'a leap year, an extra leap day is added, giving February 29 '
                                  "days.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'February has 29 days during leap years.</div></div>'}],
        'section': 'Leap Years, Calendars & Date Formats',
        'speech': '',
        'title': 'Challenge 1'},
    {   'id': 18,
        'quizzes': [   {   'ans': 1,
                           'exp': '15 - 12 = 3 days.',
                           'hint': 'Subtract the manufacturing day from the expiry day.',
                           'options': ['2 days', '3 days', '4 days', '5 days'],
                           'q': 'A carton of milk has MFG: 12/05/2024 and EXP: 15/05/2024. What is its shelf life?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Manufacturing "
                                  "date = 12 May 2024.</li><li class='mb-2 text-slate-700 leading-relaxed'>Expiry date "
                                  "= 15 May 2024.</li><li class='mb-2 text-slate-700 leading-relaxed'>Shelf life = 15 "
                                  "- 12 = 3 days.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> Shelf life is the time difference between manufacturing and '
                                  'expiry dates.</div></div>'},
                       {   'ans': 2,
                           'exp': 'Month 1 (January) + 4 months = Month 5 (May). Expiry date is 10/05/2024.',
                           'hint': 'Add 4 months to January (month 01).',
                           'options': ['10/03/2024', '10/04/2024', '10/05/2024', '10/06/2024'],
                           'q': "A packet of potato wafers manufactured on 10/01/2024 states 'Best before 4 months'. "
                                'What is the expiry date?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Manufacturing "
                                  "month = 01 (January).</li><li class='mb-2 text-slate-700 leading-relaxed'>Shelf "
                                  "life = 4 months.</li><li class='mb-2 text-slate-700 leading-relaxed'>Expiry month = "
                                  "01 + 4 = 05 (May).</li><li class='mb-2 text-slate-700 leading-relaxed'>Expiry date "
                                  "is 10/05/2024.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> Add shelf life duration in months directly to the manufacturing '
                                  'month.</div></div>'},
                       {   'ans': 1,
                           'exp': "Today's date is after the expiry date, meaning the product is expired.",
                           'hint': "Compare today's date with the expiry date printed on the label.",
                           'options': [   'Yes, it is fresh',
                                          'No, it expired 10 days ago and should not be eaten',
                                          'Yes, if heated',
                                          'Cannot be determined'],
                           'q': "If today's date is 25/08/2024 and a jar of jam has EXP: 15/08/2024, is it safe to "
                                'consume?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Expiry date = "
                                  "15 August 2024.</li><li class='mb-2 text-slate-700 leading-relaxed'>Current date = "
                                  "25 August 2024.</li><li class='mb-2 text-slate-700 leading-relaxed'>Since 25 August "
                                  "is 10 days past 15 August, the jam has expired.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Consuming expired food poses health risks.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Products past their "
                                  'expiration date must not be consumed.</div></div>'},
                       {   'ans': 1,
                           'exp': '2025 - 2023 = 2 years.',
                           'hint': 'Subtract 2023 from 2025.',
                           'options': ['1 year', '2 years', '3 years', '4 years'],
                           'q': 'A cough syrup bottle has MFG: 08/2023 and EXP: 08/2025. What is its shelf life in '
                                'years?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Manufactured = "
                                  "August 2023.</li><li class='mb-2 text-slate-700 leading-relaxed'>Expires = August "
                                  "2025.</li><li class='mb-2 text-slate-700 leading-relaxed'>Shelf life = 2025 - 2023 "
                                  "= 2 years (24 months).</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Shelf life can be expressed in years "
                                  'when month remains the same.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Amavasya is the new moon day when the Moon is completely dark.',
                           'hint': 'Recall the Sanskrit word for the dark moonless night.',
                           'options': ['Purnima', 'Amavasya', 'Ekadashi', 'Sankranti'],
                           'q': 'In the traditional Indian lunar calendar, what is the new moon day (night of no moon) '
                                'called?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>In the lunar "
                                  'cycle, the day the Moon is between the Earth and Sun and invisible from Earth is '
                                  "Amavasya.</li><li class='mb-2 text-slate-700 leading-relaxed'>Purnima is the night "
                                  "of the full, glowing moon.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Amavasya = New Moon (dark night); "
                                  'Purnima = Full Moon (bright night).</div></div>'},
                       {   'ans': 1,
                           'exp': 'Purnima is the full moon night.',
                           'hint': 'Recall the Sanskrit word meaning full or complete illumination.',
                           'options': ['Amavasya', 'Purnima', 'Pratipada', 'Chaturthi'],
                           'q': 'What is the glowing full moon night called in traditional Indian community calendars?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>When the Moon "
                                  'is fully illuminated as seen from Earth, the night is celebrated as '
                                  "Purnima.</li><li class='mb-2 text-slate-700 leading-relaxed'>Many Indian festivals "
                                  'like Raksha Bandhan and Guru Purnima fall on Purnima.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Purnima marks the "
                                  'peak of the bright waxing fortnight.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Krishna Paksha is the dark waning fortnight from full moon to new moon.',
                           'hint': 'This fortnight is named after darkness or darkening phase.',
                           'options': ['Shukla Paksha', 'Krishna Paksha', 'Chaitra', 'Samvat'],
                           'q': 'What is the fortnight of the waning (fading) moon called in the Indian lunar '
                                'calendar?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The lunar "
                                  "month is split into two halves of 15 days each.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Shukla Paksha is the waxing fortnight (growing brighter towards "
                                  "Purnima).</li><li class='mb-2 text-slate-700 leading-relaxed'>Krishna Paksha is the "
                                  'waning fortnight (growing darker towards Amavasya).</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Krishna Paksha = "
                                  'waning dark fortnight; Shukla Paksha = waxing bright fortnight.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Ramadan is the ninth month of the Islamic lunar calendar.',
                           'hint': 'This ninth month is followed by Eid al-Fitr.',
                           'options': ['Muharram', 'Ramadan', 'Shawwal', 'Safar'],
                           'q': 'Which Islamic calendar month is famous for the holy period of fasting from dawn to '
                                'sunset?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The Islamic "
                                  "Hijri calendar is a purely lunar calendar.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Ramadan is the sacred month of fasting observed by Muslims "
                                  "worldwide.</li><li class='mb-2 text-slate-700 leading-relaxed'>The sighting of the "
                                  'new crescent moon marks the start and end of Ramadan.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> The Islamic calendar "
                                  'follows pure lunar cycles of 354 or 355 days per year.</div></div>'},
                       {   'ans': 0,
                           'exp': '12 × 29.5 = 354 days, about 11 days shorter than a solar year.',
                           'hint': 'Multiply 12 by 29.5 to find the total lunar days.',
                           'options': ['354 days', '365 days', '366 days', '370 days'],
                           'q': 'How many days are in a typical lunar year (12 lunar months of ~29.5 days)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Each lunar "
                                  "month is about 29.5 days.</li><li class='mb-2 text-slate-700 leading-relaxed'>For "
                                  "12 lunar months: 12 × 29.5 = 354 days.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>This is approximately 11 days shorter than the 365-day solar "
                                  "year.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'A lunar year of 354 days is about 11 days shorter than a solar year.</div></div>'},
                       {   'ans': 1,
                           'exp': 'The 11-day difference causes lunar events to rotate forward through the solar '
                                  'seasons.',
                           'hint': 'Find the difference between 365 days and 354 days.',
                           'options': [   'Because clocks stop',
                                          'Because the lunar year (354 days) is 11 days shorter than the solar year '
                                          '(365 days)',
                                          'Because of leap years',
                                          'By international vote'],
                           'q': 'Why do festivals based on pure lunar calendars (like Eid) shift by about 11 days each '
                                'year on the solar Gregorian calendar?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Solar year = "
                                  "365 days.</li><li class='mb-2 text-slate-700 leading-relaxed'>Lunar year = 354 "
                                  "days.</li><li class='mb-2 text-slate-700 leading-relaxed'>Difference = 365 - 354 = "
                                  "11 days.</li><li class='mb-2 text-slate-700 leading-relaxed'>Because of this 11-day "
                                  'shortfall, lunar calendar dates occur 11 days earlier in each successive solar '
                                  "year.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'The 11-day annual gap causes pure lunar festivals to cycle through all four '
                                  'seasons.</div></div>'}],
        'section': 'Expiry Dates & Community Lunar Calendars',
        'speech': '',
        'title': 'Challenge 2'},
    {   'id': 19,
        'quizzes': [   {   'ans': 2,
                           'exp': '7:30 PM + 12:00 = 19:30 hours.',
                           'hint': 'Add 12 to PM hours: 7 + 12 = 19.',
                           'options': ['07:30 hours', '17:30 hours', '19:30 hours', '21:30 hours'],
                           'q': 'How is 7:30 PM written in the 24-hour digital clock format?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>To convert PM "
                                  "times to 24-hour time, add 12 to the hour.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>7 + 12 = 19.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The minutes remain unchanged: 30.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Result = 19:30 hours.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Rule: Add 12 to the "
                                  'hours for any time between 1:00 PM and 11:59 PM.</div></div>'},
                       {   'ans': 1,
                           'exp': '23:45 - 12:00 = 11:45 PM.',
                           'hint': 'Subtract 12 from hours greater than 12: 23 - 12 = 11.',
                           'options': ['11:45 AM', '11:45 PM', '10:45 PM', '9:45 PM'],
                           'q': 'A railway departure board shows a train leaving at 23:45 hours. What time is this in '
                                '12-hour AM/PM format?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The hour is "
                                  "23, which is greater than 12.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Subtract 12: 23 - 12 = 11.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Because the original time was after 12:00 noon, it is PM.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Result = 11:45 PM.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Rule: Subtract 12 "
                                  'from hours greater than 12 to find PM time.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Midnight marks both the end of one day (24:00) and the start of the next (00:00).',
                           'hint': 'Midnight resets the hours back to zero to begin the day.',
                           'options': ['12:00 hours', '24:00 hours (or 00:00 hours)', '01:00 hours', '00:12 hours'],
                           'q': 'What is 12:00 midnight in 24-hour digital time notation?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Midnight marks "
                                  "the start of a new calendar day.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>In 24-hour format, it is written as 00:00 hours (or 24:00 hours at "
                                  "the conclusion of a schedule).</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> 00:00 hours represents the start of "
                                  'a brand new day.</div></div>'},
                       {   'ans': 2,
                           'exp': '3/4 × 60 minutes = 45 minutes.',
                           'hint': '1/4 hour = 15 minutes; 3 × 15 = 45 minutes.',
                           'options': ['30 minutes', '40 minutes', '45 minutes', '50 minutes'],
                           'q': 'How many minutes are in 3/4 (three-quarters) of an hour?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>1 full hour = "
                                  "60 minutes.</li><li class='mb-2 text-slate-700 leading-relaxed'>1/4 of an hour = 60 "
                                  "÷ 4 = 15 minutes.</li><li class='mb-2 text-slate-700 leading-relaxed'>3/4 of an "
                                  "hour = 3 × 15 = 45 minutes.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Three-quarters of an hour equals 45 "
                                  'minutes.</div></div>'},
                       {   'ans': 2,
                           'exp': '30 ÷ 60 = 1/2 of an hour.',
                           'hint': '30 is half of 60.',
                           'options': ['1/4', '1/3', '1/2', '3/4'],
                           'q': 'What fraction of an hour is represented by 30 minutes?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Total minutes "
                                  "in an hour = 60.</li><li class='mb-2 text-slate-700 leading-relaxed'>Fraction = "
                                  "30/60.</li><li class='mb-2 text-slate-700 leading-relaxed'>Simplifying: 30 ÷ 30 = "
                                  "1, 60 ÷ 30 = 2.</li><li class='mb-2 text-slate-700 leading-relaxed'>Fraction = 1/2 "
                                  "(half an hour).</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> 30 minutes is exactly half of an hour (1/2 hour).</div></div>'},
                       {   'ans': 2,
                           'exp': 'From 2:15 to 3:00 is 45 minutes (three-quarters of an hour).',
                           'hint': 'Count from 2:15 to 3:00.',
                           'options': ['30 minutes', '40 minutes', '45 minutes', '1 hour'],
                           'q': 'A school sports period begins at 2:15 PM and ends at 3:00 PM. How long was the '
                                'period?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Start time = "
                                  "2:15 PM.</li><li class='mb-2 text-slate-700 leading-relaxed'>End time = 3:00 "
                                  "PM.</li><li class='mb-2 text-slate-700 leading-relaxed'>From 2:15 to 3:00 is 60 - "
                                  "15 = 45 minutes.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> From 15 minutes past the hour to the next hour is 45 '
                                  'minutes.</div></div>'},
                       {   'ans': 1,
                           'exp': '6:45 PM + 2 hours = 8:45 PM; 8:45 PM + 15 min = 9:00 PM.',
                           'hint': 'Add 2 hours first (8:45 PM), then add 15 minutes.',
                           'options': ['8:45 PM', '9:00 PM', '9:15 PM', '9:30 PM'],
                           'q': 'If a movie starts at 6:45 PM and runs for 2 hours and 15 minutes, at what time does '
                                'it finish?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Start = 6:45 "
                                  "PM.</li><li class='mb-2 text-slate-700 leading-relaxed'>Add 2 hours: 6:45 + 2h = "
                                  "8:45 PM.</li><li class='mb-2 text-slate-700 leading-relaxed'>Add remaining 15 "
                                  "minutes: 8:45 + 15m = 9:00 PM.</li></ol></div><div class='bg-amber-50 border-l-4 "
                                  'border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Add hours first, then advance the "
                                  'remaining minutes to the next hour.</div></div>'},
                       {   'ans': 1,
                           'exp': '24 - (8 + 6 + 2) = 24 - 16 = 8 hours remaining.',
                           'hint': 'Total day = 24 hours. Subtract 8 + 6 + 2 = 16.',
                           'options': ['6 hours', '8 hours', '10 hours', '12 hours'],
                           'q': 'On a 24-hour daily routine wheel, if a student spends 8 hours sleeping, 6 hours at '
                                'school, and 2 hours studying, how many hours remain for other activities?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Total hours in "
                                  "a day = 24.</li><li class='mb-2 text-slate-700 leading-relaxed'>Allocated hours = 8 "
                                  "(sleep) + 6 (school) + 2 (study) = 16 hours.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Remaining hours = 24 - 16 = 8 hours.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> All daily activities "
                                  'must sum to exactly 24 hours on a complete day wheel.</div></div>'},
                       {   'ans': 1,
                           'exp': "'Half past 9' means 30 minutes after 9:00, which is 9:30.",
                           'hint': 'Half of 60 minutes is 30 minutes.',
                           'options': ['9:15', '9:30', '9:45', '10:30'],
                           'q': "What does 'half past 9' mean in digital time notation?",
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>'Half past' "
                                  'signifies that half an hour (30 minutes) has elapsed after the hour.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>Half past 9 = 9:30.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> 'Half past' always "
                                  'indicates 30 minutes past the designated hour.</div></div>'},
                       {   'ans': 2,
                           'exp': '360° ÷ 4 = 90° (a right angle).',
                           'hint': 'A full circle is 360°. One quarter is 360° ÷ 4.',
                           'options': ['45°', '60°', '90°', '180°'],
                           'q': 'How many degrees does the minute hand turn in 15 minutes (a quarter hour)?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>A full clock "
                                  "face circle = 360 degrees.</li><li class='mb-2 text-slate-700 leading-relaxed'>15 "
                                  "minutes is 1/4 of a full circle (60 minutes).</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>360° ÷ 4 = 90 degrees.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The hands form a perfect right angle at quarter "
                                  "hours.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'A quarter-turn of the minute hand traverses exactly 90 degrees.</div></div>'}],
        'section': '24-Hour Clocks, AM/PM & Fractional Hours',
        'speech': '',
        'title': 'Challenge 3'},
    {   'id': 20,
        'quizzes': [   {   'ans': 2,
                           'exp': 'Hour is 3, minute is 6 × 5 = 30. Time is 3:30.',
                           'hint': 'The short hand shows the hour (3), and the long hand at 6 shows minutes: 6 × 5 = '
                                   '30.',
                           'options': ['6:03', '3:06', '3:30', '6:15'],
                           'q': 'A clock shows the short hour hand pointing just past 3 and the long minute hand '
                                'pointing to 6. What time is it?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The short hand "
                                  "is the hour hand; it is between 3 and 4, indicating hour 3.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>The long hand is the minute hand; it points to "
                                  "6.</li><li class='mb-2 text-slate-700 leading-relaxed'>Each number on the dial "
                                  "represents 5 minutes: 6 × 5 = 30 minutes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The correct time is 3:30.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Never confuse the hour hand with the "
                                  'minute hand; multiply minute hand number by 5.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Numbers on a clock represent 5-minute increments: 8 × 5 = 40 minutes.',
                           'hint': 'Remember each clock number represents 5 minutes for the minute hand.',
                           'options': [   'Because 8 means 40 minutes (8 × 5 = 40)',
                                          'Because 8 means 80 minutes',
                                          'Because 4:08 is impossible',
                                          "Because clocks don't have 8"],
                           'q': "Why is it an error to say a clock reads '4:08' when the minute hand points to 8?",
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The numbers 1 "
                                  'to 12 on a clock dial represent 5-minute chunks for the minute hand.</li><li '
                                  "class='mb-2 text-slate-700 leading-relaxed'>When the minute hand points to 8, "
                                  "elapsed minutes = 8 × 5 = 40 minutes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>The time is 4:40, not 4:08.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> Minute hand at N represents N × 5 "
                                  'minutes.</div></div>'},
                       {   'ans': 1,
                           'exp': 'Before midnight = 2h 30m; After midnight = 5h 15m. Total = 7 hours 45 minutes.',
                           'hint': 'Calculate time before midnight (21:30 to 24:00) + time after midnight (00:00 to '
                                   '05:15).',
                           'options': [   '7 hours 15 minutes',
                                          '7 hours 45 minutes',
                                          '8 hours 15 minutes',
                                          '8 hours 45 minutes'],
                           'q': 'A passenger train departs city A at 21:30 and arrives at city B at 05:15 the '
                                'following morning. What is the total travel duration?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Before "
                                  "midnight: from 21:30 to 24:00 is 2 hours and 30 minutes.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>After midnight: from 00:00 to 05:15 is 5 hours and "
                                  "15 minutes.</li><li class='mb-2 text-slate-700 leading-relaxed'>Add both parts: 2h "
                                  "30m + 5h 15m = 7 hours and 45 minutes.</li></ol></div><div class='bg-amber-50 "
                                  'border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 '
                                  "leading-normal'><strong>Key Takeaway:</strong> For overnight journeys, split the "
                                  'calculation at midnight (24:00).</div></div>'},
                       {   'ans': 1,
                           'exp': '21 ÷ 7 = 3 full weeks with 0 remainder. The day remains Friday.',
                           'hint': '22 - 1 = 21 days. 21 is a multiple of 7 (3 weeks).',
                           'options': ['Thursday', 'Friday', 'Saturday', 'Sunday'],
                           'q': 'If the 1st of May is a Friday, what day of the week will the 22nd of May be?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Start date = 1 "
                                  "May (Friday).</li><li class='mb-2 text-slate-700 leading-relaxed'>Target date = 22 "
                                  "May.</li><li class='mb-2 text-slate-700 leading-relaxed'>Days elapsed = 22 - 1 = 21 "
                                  "days.</li><li class='mb-2 text-slate-700 leading-relaxed'>21 ÷ 7 = exactly 3 weeks "
                                  "with 0 days remainder.</li><li class='mb-2 text-slate-700 leading-relaxed'>Since "
                                  'the remainder is 0, the day of the week is still Friday.</li></ol></div><div '
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Adding any exact "
                                  'multiple of 7 days lands on the identical day of the week.</div></div>'},
                       {   'ans': 0,
                           'exp': 'Century years ending in 00 must be divisible by 400. 1900 ÷ 400 = 4 remainder 300.',
                           'hint': 'Recall the special rule for century years ending in two zeros.',
                           'options': [   'Because century years must be divisible by 400 to be leap years, and 1900 '
                                          'is not',
                                          'Because February had 30 days',
                                          'Because 1900 was an odd number',
                                          'It was a leap year'],
                           'q': 'Why was the century year 1900 NOT a leap year, even though 1900 is divisible by 4?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>The Gregorian "
                                  "calendar rule states: century years ending in '00' are leap years only if divisible "
                                  "by 400.</li><li class='mb-2 text-slate-700 leading-relaxed'>1900 ÷ 400 = 4 with a "
                                  "remainder of 300.</li><li class='mb-2 text-slate-700 leading-relaxed'>Because 1900 "
                                  'is not divisible by 400, it was an ordinary year with 28 days in '
                                  "February.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Century years must be divisible by 400 to qualify as leap years.</div></div>'},
                       {   'ans': 2,
                           'exp': '3h 40m + 2h 50m = 5h 90m = 6 hours 30 minutes.',
                           'hint': '40m + 50m = 90m = 1h 30m. 3h + 2h + 1h = 6h 30m.',
                           'options': [   '5 hours 90 minutes',
                                          '6 hours 10 minutes',
                                          '6 hours 30 minutes',
                                          '6 hours 40 minutes'],
                           'q': 'Add the time durations: 3 hours 40 minutes + 2 hours 50 minutes.',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Add the "
                                  "minutes: 40 + 50 = 90 minutes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Since 90 ≥ 60, convert 60 minutes into 1 hour: 90 - 60 = 30 "
                                  "minutes remaining, with 1 hour carried.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Add the hours: 3 + 2 + 1 (carried) = 6 hours.</li><li class='mb-2 "
                                  "text-slate-700 leading-relaxed'>Total = 6 hours and 30 minutes.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> Regroup 60 minutes as "
                                  '1 hour whenever the minute sum reaches or exceeds 60.</div></div>'},
                       {   'ans': 1,
                           'exp': '4h 75m - 2h 45m = 2 hours 30 minutes.',
                           'hint': 'Borrow 1 hour (60 min) from 5 hours: 4 hours 75 minutes - 2 hours 45 minutes.',
                           'options': [   '2 hours 15 minutes',
                                          '2 hours 30 minutes',
                                          '2 hours 45 minutes',
                                          '3 hours 30 minutes'],
                           'q': 'Subtract: 5 hours 15 minutes - 2 hours 45 minutes.',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>We cannot "
                                  "subtract 45 minutes from 15 minutes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Borrow 1 hour from 5 hours: 5 hours becomes 4 hours.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Convert the borrowed hour into 60 "
                                  "minutes and add to 15: 15 + 60 = 75 minutes.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Now subtract: 75m - 45m = 30 minutes; 4h - 2h = 2 hours.</li><li "
                                  "class='mb-2 text-slate-700 leading-relaxed'>Result = 2 hours and 30 "
                                  "minutes.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'When borrowing in time subtraction, 1 borrowed hour equals 60 minutes.</div></div>'},
                       {   'ans': 2,
                           'exp': 'July (31 days) + August (31 days) = 62 days.',
                           'hint': 'Both July and August have 31 days.',
                           'options': ['60 days', '61 days', '62 days', '63 days'],
                           'q': 'How many days are there altogether in the months of July and August combined?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>July has 31 "
                                  "days.</li><li class='mb-2 text-slate-700 leading-relaxed'>August is the consecutive "
                                  "month and also has 31 days.</li><li class='mb-2 text-slate-700 leading-relaxed'>31 "
                                  "+ 31 = 62 days.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 "
                                  "p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key "
                                  'Takeaway:</strong> July and August are consecutive months that both have 31 '
                                  'days.</div></div>'},
                       {   'ans': 1,
                           'exp': '10 October + 2 days = 12 October at 06:30 hours.',
                           'hint': '48 hours = 2 full days (24 × 2 = 48).',
                           'options': [   '06:30 hours on 11 October',
                                          '06:30 hours on 12 October',
                                          '12:00 hours on 12 October',
                                          '06:30 hours on 13 October'],
                           'q': 'A bakery bakes bread at 06:30 hours. The bread remains fresh for 48 hours. By what '
                                'time and date should it be consumed if baked on 10 October?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>48 hours ÷ 24 "
                                  "hours/day = 2 full days.</li><li class='mb-2 text-slate-700 leading-relaxed'>Start "
                                  "= 06:30 hours on 10 October.</li><li class='mb-2 text-slate-700 "
                                  "leading-relaxed'>Add 2 days = 06:30 hours on 12 October.</li></ol></div><div "
                                  "class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs "
                                  "text-amber-900 leading-normal'><strong>Key Takeaway:</strong> 48 hours corresponds "
                                  'to exactly two full 24-hour days.</div></div>'},
                       {   'ans': 0,
                           'exp': '60 is a highly composite number that divides evenly into many fractions (halves, '
                                  'thirds, quarters, fifths, sixths).',
                           'hint': 'Think about how easily 60 divides into halves, thirds, and quarters.',
                           'options': [   'It is an ancient astronomical tradition from Babylonians because 60 is '
                                          'divisible by 2, 3, 4, 5, 6, 10, 12, 15, 20, 30',
                                          'Because clocks have 60 gears',
                                          'Because humans have 60 fingers',
                                          'By random accident'],
                           'q': 'Why is time measured using base 60 (60 seconds = 1 minute, 60 minutes = 1 hour) '
                                'instead of base 10?',
                           'sol': "<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 "
                                  "p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider "
                                  "text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside "
                                  "space-y-1.5 text-sm'><li class='mb-2 text-slate-700 leading-relaxed'>Ancient "
                                  'Babylonian astronomers chose 60 because it has 12 factors: 1, 2, 3, 4, 5, 6, 10, '
                                  "12, 15, 20, 30, and 60.</li><li class='mb-2 text-slate-700 leading-relaxed'>This "
                                  'makes it remarkably easy to calculate halves (30 min), thirds (20 min), quarters '
                                  '(15 min), fifths (12 min), and sixths (10 min) without fractions or '
                                  "decimals.</li></ol></div><div class='bg-amber-50 border-l-4 border-amber-500 p-3 "
                                  "rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> "
                                  'Base 60 allows convenient fractional divisions of time without messy '
                                  'decimals.</div></div>'}],
        'section': 'Clock Errors, Midnight Trains & Base-60 Math',
        'speech': '',
        'title': 'Challenge 4'}]
