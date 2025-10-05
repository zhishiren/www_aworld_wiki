// utils/timeFormatter.js  
  
export function formatTimestamp(timestamp) {  
    // 确保时间戳是以毫秒为单位
    const validTimestamp = timestamp < 1000000000000 ? timestamp * 1000 : timestamp; 
    const now = Date.now();  
    const diff = (now - validTimestamp) / 1000; // 转换为秒  
  
    if (diff < 60) {  
        return '刚刚';  
    } else if (diff < 3600) { // 60 * 60  
        return Math.floor(diff / 60) + '分钟前';  
    } else if (diff < 86400) { // 3600 * 24  
        return Math.floor(diff / 3600) + '小时前';  
    } else if (diff < 604800) { // 86400 * 7  
        return Math.floor(diff / 86400) + '天前';  
    } else if (diff < 2592000) { // 86400 * 30  
        return Math.floor(diff / 604800) + '周前';  
    } else if (diff < 31536000) { // 86400 * 365  
        return Math.floor(diff / 2592000) + '个月前';  
    } else {  
        const date = new Date(validTimestamp);  
        const year = date.getFullYear();  
        let month = date.getMonth() + 1; // getMonth()是从0开始的  
        let day = date.getDate();  
        month = month < 10 ? '0' + month : month; // 补零  
        day = day < 10 ? '0' + day : day; // 补零  
        return `${year}-${month}-${day}`; // 修改为 YYYY-MM-DD 格式
    }  
}
