// 显示最后更新时间
document.addEventListener("DOMContentLoaded", function() {
  const lastUpdated = document.createElement("div");
  lastUpdated.className = "last-updated";
  lastUpdated.innerHTML = "最后更新: " + new Date().toLocaleDateString();
  document.querySelector(".md-content").prepend(lastUpdated);
});

// 添加复制按钮
document.querySelectorAll("pre code").forEach(codeBlock => {
  const copyButton = document.createElement("button");
  copyButton.className = "copy-button";
  copyButton.title = "复制代码";
  copyButton.innerHTML = "<i class="fas fa-copy"></i>";
  
  codeBlock.parentNode.insertBefore(copyButton, codeBlock);
  
  copyButton.addEventListener("click", () => {
    navigator.clipboard.writeText(codeBlock.textContent);
    copyButton.innerHTML = "<i class="fas fa-check"></i>";
    setTimeout(() => {
      copyButton.innerHTML = "<i class="fas fa-copy"></i>";
    }, 2000);
  });
});