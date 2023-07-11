const downloadButton = document.getElementById('downloadButton');
const sourceCodeUrl = '/Users/sam/Downloads/Titanic/write.py';

downloadButton.addEventListener('click', () => {
  downloadButton.setAttribute('href', sourceCodeUrl);
  downloadButton.setAttribute('download', 'write.py');
});