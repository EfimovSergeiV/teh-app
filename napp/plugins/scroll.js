export default function({ app }) {
  if (process.client) {
    window.addEventListener('scroll', () => {
      const scrollTop = (window.pageYOffset || document.documentElement.scrollTop)/20;
      const background = document.querySelector('#background');
      if (background) {
        background.style.backgroundPositionY = `${scrollTop}px`;
      }
    });
  }
}
