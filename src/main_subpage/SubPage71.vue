<template>
  <div class="word-cloud-wrapper">
    <canvas
      ref="canvasRef"
      class="word-cloud-canvas"
      width="520"
      height="520"
    ></canvas>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';

const STATIC_WORDS = [
  { text: '志士仁人', weight: 100 },
  { text: '社区共建', weight: 98 },
  { text: '知识分享', weight: 96 },
  { text: '开放协作', weight: 95 },
  { text: '成长记录', weight: 93 },
  { text: '行动计划', weight: 92 },
  { text: '学习笔记', weight: 90 },
  { text: '项目复盘', weight: 88 },
  { text: '创新提案', weight: 87 },
  { text: '经验总结', weight: 85 },
  { text: '任务派发', weight: 84 },
  { text: '社群活动', weight: 83 },
  { text: '讨论区', weight: 82 },
  { text: '实践案例', weight: 81 },
  { text: '志愿服务', weight: 80 },
  { text: '资源清单', weight: 79 },
  { text: '问题求助', weight: 78 },
  { text: '反馈建议', weight: 77 },
  { text: '协作指南', weight: 76 },
  { text: '时间管理', weight: 75 },
  { text: '数字档案', weight: 74 },
  { text: '活动报名', weight: 73 },
  { text: '知识库', weight: 72 },
  { text: '公告板', weight: 71 },
  { text: '小组会议', weight: 70 },
  { text: '周报', weight: 69 },
  { text: '任务协同', weight: 68 },
  { text: '社群治理', weight: 67 },
  { text: '价值共创', weight: 66 },
  { text: '素养提升', weight: 65 },
  { text: '目标复盘', weight: 64 },
  { text: '共学计划', weight: 63 },
  { text: '知识地图', weight: 62 },
  { text: '资源互助', weight: 61 },
  { text: '新人引导', weight: 60 },
  { text: '公社动态', weight: 59 },
  { text: '任务反馈', weight: 58 },
  { text: '活动复盘', weight: 57 },
  { text: '线上沙龙', weight: 56 },
  { text: '线下聚会', weight: 55 },
  { text: '项目筹备', weight: 54 },
  { text: '流程共建', weight: 53 },
  { text: '成果发表', weight: 52 },
  { text: '共创手记', weight: 51 },
  { text: '团队默契', weight: 50 },
  { text: '角色分工', weight: 49 },
  { text: '任务看板', weight: 48 },
  { text: '协作礼仪', weight: 47 },
  { text: '答疑直播', weight: 46 },
  { text: '行动打卡', weight: 45 },
  { text: '社区守则', weight: 44 },
  { text: '每日灵感', weight: 43 },
  { text: '资料归档', weight: 42 },
  { text: '成员风采', weight: 41 },
  { text: '公告提醒', weight: 40 },
  { text: '案例征集', weight: 39 },
  { text: '共创实验', weight: 38 },
  { text: '技能互换', weight: 37 },
  { text: '社区巡礼', weight: 36 },
  { text: '伙伴招募', weight: 35 },
  { text: '共读计划', weight: 34 },
  { text: '节气活动', weight: 33 },
  { text: '知识测验', weight: 32 },
  { text: '周末分享', weight: 31 },
  { text: '创客市集', weight: 30 },
  { text: '灵感墙', weight: 29 },
  { text: '学习打卡', weight: 28 },
  { text: '协作手册', weight: 27 },
  { text: '夜读之约', weight: 26 },
  { text: '晨间例会', weight: 25 },
  { text: '值班日志', weight: 24 },
  { text: '微课输出', weight: 23 },
  { text: '主题共创', weight: 22 },
  { text: '资源众筹', weight: 21 },
  { text: '设计提案', weight: 20 },
  { text: '志愿清单', weight: 19 },
  { text: '互助问答', weight: 18 },
  { text: '议题征集', weight: 17 },
  { text: '成员访谈', weight: 16 },
  { text: '公社相册', weight: 15 },
  { text: '活动总结', weight: 14 },
  { text: '经验笔记', weight: 13 },
  { text: '共创备忘', weight: 12 },
  { text: '资料索引', weight: 11 },
  { text: '周计划', weight: 10 },
  { text: '月度目标', weight: 9 },
  { text: '协作排班', weight: 8 },
  { text: '成果展示', weight: 7 },
  { text: '入社问卷', weight: 6 },
  { text: '社区问候', weight: 5 },
  { text: '城市分社', weight: 4 },
  { text: '年度承诺', weight: 3 },
  { text: '共创纪念', weight: 2 },
  { text: '灵感速递', weight: 1 }
];

const COLOR_PALETTE = [
  '#5B8FF9',
  '#61DDAA',
  '#65789B',
  '#F6BD16',
  '#FF9D4D',
  '#D3ADF7',
  '#78D3F8',
  '#B37FEB'
];

const FONT_FAMILY = '"Microsoft YaHei", "PingFang SC", "Helvetica Neue", sans-serif';
const MIN_FONT_SIZE = 12;
const MAX_FONT_SIZE = 34;
const GOLDEN_ANGLE = Math.PI * (3 - Math.sqrt(5));

function buildLetterPaths(cx, cy, radius) {
  const height = radius * 1.4;
  const halfWidth = radius * 0.82;
  const innerOffset = radius * 0.28;
  const baseY = cy + height / 2;
  const topY = cy - height / 2;

  const outer = new Path2D();
  outer.moveTo(cx - halfWidth, baseY);
  outer.lineTo(cx, topY);
  outer.lineTo(cx + halfWidth, baseY);
  outer.lineTo(cx + halfWidth - innerOffset, baseY);
  outer.lineTo(cx, topY + innerOffset);
  outer.lineTo(cx - halfWidth + innerOffset, baseY);
  outer.closePath();

  const crossThickness = radius * 0.2;
  const crossWidth = halfWidth * 1.18;
  const crossY = cy + height * 0.05;
  const cross = new Path2D();
  cross.rect(cx - crossWidth / 2, crossY - crossThickness / 2, crossWidth, crossThickness);

  const solid = new Path2D();
  solid.addPath(outer);
  solid.addPath(cross);

  return {
    outer,
    cross,
    solid
  };
}

function mapWeightToFont(weight, minWeight, maxWeight) {
  if (maxWeight === minWeight) {
    return (MIN_FONT_SIZE + MAX_FONT_SIZE) / 2;
  }
  const ratio = (weight - minWeight) / (maxWeight - minWeight);
  return Math.round(MIN_FONT_SIZE + ratio * (MAX_FONT_SIZE - MIN_FONT_SIZE));
}

function pickColor(weight, minWeight, maxWeight) {
  if (maxWeight === minWeight) {
    return COLOR_PALETTE[0];
  }
  const ratio = (weight - minWeight) / (maxWeight - minWeight);
  const index = Math.min(
    COLOR_PALETTE.length - 1,
    Math.floor(ratio * COLOR_PALETTE.length)
  );
  return COLOR_PALETTE[index];
}

function isBoxInsideCircle(box, center, radius) {
  const corners = [
    [box.left, box.top],
    [box.left, box.bottom],
    [box.right, box.top],
    [box.right, box.bottom]
  ];
  return corners.every(([x, y]) => {
    const dx = x - center.x;
    const dy = y - center.y;
    return Math.sqrt(dx * dx + dy * dy) <= radius;
  });
}

function intersectsForbiddenArea(ctx, box, letterPaths) {
  const points = [
    [(box.left + box.right) / 2, (box.top + box.bottom) / 2],
    [box.left, (box.top + box.bottom) / 2],
    [box.right, (box.top + box.bottom) / 2],
    [(box.left + box.right) / 2, box.top],
    [(box.left + box.right) / 2, box.bottom],
    [box.left, box.top],
    [box.right, box.top],
    [box.left, box.bottom],
    [box.right, box.bottom]
  ];
  return points.some(([x, y]) => ctx.isPointInPath(letterPaths.solid, x, y));
}

function collidesExisting(box, placedItems) {
  const padding = 2.5;
  return placedItems.some((item) => {
    const target = item.box;
    return !(
      box.right + padding < target.left ||
      box.left - padding > target.right ||
      box.bottom + padding < target.top ||
      box.top - padding > target.bottom
    );
  });
}

function layoutWords(ctx, words, center, radius, letterPaths) {
  const sorted = [...words].sort((a, b) => b.weight - a.weight);
  if (!sorted.length) {
    return [];
  }

  const minWeight = sorted[sorted.length - 1].weight;
  const maxWeight = sorted[0].weight;
  const placements = [];

  sorted.forEach((word, index) => {
    const progression = index / Math.max(sorted.length - 1, 1);
    const bandInner = radius * (0.18 + progression * 0.63);
    const bandOuter = radius - 6;

    const fontSize = mapWeightToFont(word.weight, minWeight, maxWeight);
    const font = `600 ${fontSize}px ${FONT_FAMILY}`;
    ctx.font = font;
    const textWidth = ctx.measureText(word.text).width;
    const halfWidth = textWidth / 2 + 1.8;
    const halfHeight = fontSize / 2 + 2;
    const maxRadius = Math.max(bandOuter - Math.max(halfWidth, halfHeight), bandInner);

    for (let attempt = 0; attempt < 2000; attempt += 1) {
      const radialOffset = Math.sqrt(attempt) * (3.4 + fontSize / 18);
      const candidateRadius = Math.min(maxRadius, bandInner + radialOffset);
      const theta = (index * 11 + attempt) * GOLDEN_ANGLE;
      const px = center.x + candidateRadius * Math.cos(theta);
      const py = center.y + candidateRadius * Math.sin(theta);

      const box = {
        left: px - halfWidth,
        right: px + halfWidth,
        top: py - halfHeight,
        bottom: py + halfHeight
      };

      if (!isBoxInsideCircle(box, center, radius)) continue;
      const distance = Math.hypot(px - center.x, py - center.y);
      if (distance < radius * 0.16) continue;
      if (intersectsForbiddenArea(ctx, box, letterPaths)) continue;
      if (collidesExisting(box, placements)) continue;

      placements.push({
        text: word.text,
        weight: word.weight,
        font,
        color: pickColor(word.weight, minWeight, maxWeight),
        x: px,
        y: py,
        box
      });
      break;
    }
  });

  return placements;
}

function renderWordCloud(canvas, words) {
  if (!canvas) return;
  const parent = canvas.parentElement;
  const parentWidth = parent ? parent.clientWidth : canvas.width;
  const fallbackSize = canvas.clientWidth || canvas.width || 480;
  const availableWidth = parentWidth || fallbackSize;
  const baseSize = Math.max(Math.min(availableWidth, 560), 320);

  const dpr = window.devicePixelRatio || 1;
  canvas.width = baseSize * dpr;
  canvas.height = baseSize * dpr;
  canvas.style.width = `${baseSize}px`;
  canvas.style.height = `${baseSize}px`;

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.scale(dpr, dpr);
  ctx.clearRect(0, 0, baseSize, baseSize);
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';

  const center = { x: baseSize / 2, y: baseSize / 2 };
  const radius = baseSize * 0.46;
  const circlePath = new Path2D();
  circlePath.arc(center.x, center.y, radius, 0, Math.PI * 2);
  const letterPaths = buildLetterPaths(center.x, center.y, radius * 0.68);

  ctx.save();
  ctx.fillStyle = 'rgba(255, 255, 255, 0.04)';
  ctx.fill(circlePath);
  ctx.restore();

  ctx.save();
  ctx.clip(circlePath);
  const placements = layoutWords(ctx, words, center, radius, letterPaths);
  placements.forEach((item) => {
    ctx.save();
    ctx.font = item.font;
    ctx.fillStyle = item.color;
    ctx.fillText(item.text, item.x, item.y);
    ctx.restore();
  });
  ctx.restore();

  ctx.save();
  ctx.globalCompositeOperation = 'destination-out';
  ctx.fill(letterPaths.solid);
  ctx.restore();

  ctx.save();
  ctx.strokeStyle = 'rgba(91, 143, 249, 0.6)';
  ctx.lineWidth = 2;
  ctx.stroke(circlePath);
  ctx.stroke(letterPaths.solid);
  ctx.restore();
}

export default {
  name: 'SubPage71',
  setup() {
    const canvasRef = ref(null);
    let resizeTimer = null;
    let frameId = null;

    const queueRender = () => {
      if (!canvasRef.value) return;
      if (frameId) {
        cancelAnimationFrame(frameId);
      }
      frameId = requestAnimationFrame(() => {
        renderWordCloud(canvasRef.value, STATIC_WORDS);
      });
    };

    const handleResize = () => {
      if (resizeTimer) {
        clearTimeout(resizeTimer);
      }
      resizeTimer = setTimeout(() => {
        queueRender();
      }, 140);
    };

    onMounted(() => {
      queueRender();
      window.addEventListener('resize', handleResize);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', handleResize);
      if (resizeTimer) {
        clearTimeout(resizeTimer);
      }
      if (frameId) {
        cancelAnimationFrame(frameId);
      }
    });

    return {
      canvasRef
    };
  }
};
</script>

<style scoped>
.word-cloud-wrapper {
  width: 100%;
  padding: 24px;
  display: flex;
  justify-content: center;
  box-sizing: border-box;
}

.word-cloud-canvas {
  width: min(100%, 560px);
  max-width: 560px;
  aspect-ratio: 1 / 1;
  display: block;
}

@media (max-width: 600px) {
  .word-cloud-wrapper {
    padding: 16px;
  }
}
</style>
