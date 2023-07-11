document.addEventListener('DOMContentLoaded', () => {
    const rectangleGroups = document.querySelectorAll('.rectangle-group');
  
    rectangleGroups.forEach((group) => {
      const rect = group.querySelector('rect');
      const percentageText = group.querySelector('.percentage-text');
  
      group.addEventListener('mouseenter', () => {
        rect.classList.add('rect-animation');
        percentageText.style.opacity = '1';
      });
  
      group.addEventListener('mouseleave', () => {
        rect.classList.remove('rect-animation');
        percentageText.style.opacity = '0';
      });
    });
  });
  