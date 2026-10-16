config.load_autoconfig(False)

config.source("themes/city-lights-theme.py")  

c.auto_save.session = True
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'g': 'https://google.com/search?q={}',
    
    'yt': 'https://youtube.com/results?search_query={}',
    'ytm': 'https://music.youtube.com/search?q={}',

    'np': 'https://search.nixos.org/packages?query={}',
    
    'tt': 'https://tiktok.com/@{}',
    'ig': 'https://instagram.com/{}',
    'th': 'https://threads.com/@{}',
}

c.completion.height = '15%'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = 'dark'

config.bind('m', 'spawn mpv {url}')
config.bind('M', 'hint links spawn mpv {hint-url}')

config.bind('<ctrl-n>', 'scroll down')
config.bind('<ctrl-p>', 'scroll up')
# config.bind('<ctrl-g>', 'leave-mode')

config.bind('<ctrl-n>', 'completion-item-focus next', mode='command')
config.bind('<ctrl-p>', 'completion-item-focus prev', mode='command')
config.bind('<ctrl-g>', 'leave-mode', mode='command')
config.bind('<alt-n>', 'command-history-next', mode='command')
config.bind('<alt-p>', 'command-history-prev', mode='command')
