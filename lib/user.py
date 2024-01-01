from utils.fetch import fetchData, endpoint
from utils.load_components import animation, font, svg_template
from lib.chart import svgDonutChart

class User:
    def __init__(self, username, theme):
        self.username = username
        self.theme = theme


    def fetchData(self):
        rejected_attr = ['status', 'retrieved', 'reputation', 'contributionPoints']
        data = fetchData(endpoint(self.username))

        # map data to object, ignoring rejected attributes  
        for v in data.items():
            if v[0] not in rejected_attr:
                setattr(self, v[0], v[1])

        # stops DivisionByZero error.
        if (data['status'] == 'error'):
            self.username = "User not found"
            self.solvedDeg = 0.1
        else:
            self.solvedDeg = (self.totalSolved / self.totalQuestions) * 360

        print(data.keys)
        self.__generateSVG__()

    def __generateSVG__(self):
        # font
        # &quot;emRQOkaDi8w1:::IBM Plex Mono&quot;
        self.svg = svg_template.format(
            username=self.username,
            rank=self.ranking,  
            easy=f"{self.easySolved} / {self.totalEasy}", 
            medium=f"{self.mediumSolved} / {self.totalMedium}", 
            hard=f"{self.hardSolved} / {self.totalHard}", 
            chart=svgDonutChart(235,15, self.theme, 75, 10, self.solvedDeg, 150),
            acceptanceRate=f"{self.acceptanceRate}%",
            theme = self.theme,
            animation = animation,
            font = font
        )

    

