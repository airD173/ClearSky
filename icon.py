def main(icon):
    twemoji = None
    try:
        if icon == 'https://api.weather.gov/icons/land/day/skc?size=medium' or icon == 'https://api.weather.gov/icons/land/night/skc?size=medium' or icon == 'https://api.weather.gov/icons/land/day/wind_skc?size=medium' or icon == 'https://api.weather.gov/icons/land/night/wind_skc?size=medium' or icon == 'https://api.weather.gov/icons/land/day/few?size=medium' or icon == 'https://api.weather.gov/icons/land/night/few?size=medium' or icon == 'https://api.weather.gov/icons/land/day/wind_few?size=medium' or icon == 'https://api.weather.gov/icons/land/night/wind_few?size=medium':
            #Sunny
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2600.png'
        elif icon.startswith('https://api.weather.gov/icons/land/day/sct') or icon.startswith('https://api.weather.gov/icons/land/night/sct') or icon.startswith('https://api.weather.gov/icons/land/day/wind_sct') or icon.startswith('https://api.weather.gov/icons/land/night/wind_sct'):
            #Partly Cloudy
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/26c5.png'
        elif icon.startswith('https://api.weather.gov/icons/land/day/bkn') or icon.startswith('https://api.weather.gov/icons/land/night/bkn') or icon.startswith('https://api.weather.gov/icons/land/day/wind_bkn') or icon.startswith('https://api.weather.gov/icons/land/night/wind_bkn'):
            #Mostly Cloudy
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f325.png'
        elif icon == 'https://api.weather.gov/icons/land/day/ovc?size=medium' or icon == 'https://api.weather.gov/icons/land/night/ovc?size=medium' or icon == 'https://api.weather.gov/icons/land/day/wind_ovc?size=medium' or icon == 'https://api.weather.gov/icons/land/night/wind_ovc?size=medium':
            #Cloudy
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2601.png'
        elif icon == 'https://api.weather.gov/icons/land/day/snow?size=medium' or icon == 'https://api.weather.gov/icons/land/night/snow?size=medium' or icon == 'https://api.weather.gov/icons/land/day/rain_snow?size=medium' or icon == 'https://api.weather.gov/icons/land/night/rain_snow?size=medium' or icon == 'https://api.weather.gov/icons/land/day/snow_sleet?size=medium' or icon == 'https://api.weather.gov/icons/land/night/snow_sleet?size=medium' or icon == 'https://api.weather.gov/icons/land/day/fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/night/fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/day/rain_fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/night/rain_fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/day/snow_fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/night/snow_fzra?size=medium' or icon == 'https://api.weather.gov/icons/land/day/sleet?size=medium' or icon == 'https://api.weather.gov/icons/land/night/sleet?size=medium':
            #Snow
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/2744.png'
        elif icon.startswith('https://api.weather.gov/icons/land/day/rain') or icon.startswith('https://api.weather.gov/icons/land/night/rain') or icon.startswith('https://api.weather.gov/icons/land/day/rain_showers') or icon.startswith('https://api.weather.gov/icons/land/night/rain_showers'):
            #Rain
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f327.png'
        elif icon.startswith('https://api.weather.gov/icons/land/day/tsra') or icon.startswith('https://api.weather.gov/icons/land/night/tsra'):
            #Thunderstorm
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/26c8.png'
        elif icon.startswith('https://api.weather.gov/icons/land/day/fog') or icon.startswith('https://api.weather.gov/icons/land/night/fog'):
            #Fog
            twemoji = 'https://raw.githubusercontent.com/twitter/twemoji/master/assets/72x72/1f32b.png'
    except:
        print(icon)
    
    return(twemoji)