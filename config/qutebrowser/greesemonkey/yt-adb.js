document.addEventListener('load', () => {
  const btn = document.querySelector('.videoAdUiSkipButton,button#skip-button')
  const ad = [...document.querySelectorAll('.ad-showing')][0]
  
  if (btn) btn.click()
  if (ad) document.querySelector('video').currentTime = 9999999999
}, true)
