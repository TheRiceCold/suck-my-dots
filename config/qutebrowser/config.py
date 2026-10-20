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

c.content.javascript.log_message.excludes = {
    'userscript:_qute_js': ['*TrustedHTML*']
}

c.completion.height = '15%'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.preferred_color_scheme = 'dark'

ESC_BIND = 'mode-enter normal'

config.bind('<ctrl-s>', 'cmd-set-text /')
config.bind('<alt-x>', 'cmd-set-text :')
config.bind('<alt-g>', ESC_BIND)

config.bind('m', 'spawn mpv {url}')
config.bind('M', 'hint links spawn mpv {hint-url}')

config.bind('<ctrl-n>', 'scroll down')
config.bind('<ctrl-p>', 'scroll up')

# Insert Bindings
config.bind('<ctrl-y>', 'fake-key <ctrl-v>', mode='insert')
config.bind('<ctrl-x><u>', 'fake-key <ctrl-z>', mode='insert')
config.bind('<ctrl-p>', 'fake-key <up>', mode='insert')
config.bind('<ctrl-n>', 'fake-key <down>', mode='insert')

# Command Bindings
config.bind('<ctrl-g>', ESC_BIND, mode='command')
config.bind('<ctrl-s>', 'search-next', mode='command')
config.bind('<ctrl-r>', 'search-prev', mode='command')
config.bind('<ctrl-n>', 'completion-item-focus next', mode='command')
config.bind('<ctrl-p>', 'completion-item-focus prev', mode='command')
config.bind('<alt-n>', 'command-history-next', mode='command')
config.bind('<alt-p>', 'command-history-prev', mode='command')

config.bind('<ctrl-g>', ESC_BIND, mode='caret')
