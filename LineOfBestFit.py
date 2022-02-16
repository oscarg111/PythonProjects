from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

x = client.regular_season_player_box_scores(
    player_identifier="adebaba01",
    season_end_year=2021,
    output_type=OutputType.CSV,
    output_file_path="C:\\Users\\oscar\\OneDrive\\Documents\\python text files\\adebayo.csv"
)


