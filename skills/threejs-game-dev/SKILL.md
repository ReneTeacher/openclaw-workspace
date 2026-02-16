---
name: threejs-game-dev
description: 整3D遊戲同角色 - Three.js遊戲開發、Ready Player Me 3D Avatar整合、精靈動畫
metadata:
  updated: "2026-02-15"
  emoji: 🎮
---

# Three.js Game Dev Skill

整3D遊戲、角色、動畫既Skills

---

## 🎯 用途

1. **整3D Dashboard** - 似遊戲既Web介面
2. **3D角色** - 可郁既動畫角色
3. **Ready Player Me** - 生成3D Avatar

---

## 🔧 工具

### Ready Player Me

**網站:** https://readyplayer.me/

**整Avatar:**
1. 去 https://readyplayer.me/
2. 整動物/角色Avatar
3. 拎GLB URL

**Three.js Load:**
```javascript
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const loader = new GLTFLoader();
loader.load('https://models.readyplayer.me/AVATAR_ID.glb', (gltf) => {
    scene.add(gltf.scene);
});
```

### Three.js Resources

| Resource | Link |
|----------|------|
| Sprite Animation | https://github.com/tamani-coding/threejs-sprite-flipbook |
| Boilerplate | https://github.com/egemenertugrul/wolf3d-readyplayerme-threejs-boilerplate |
| Examples | https://threejs.org/examples/ |

---

## 📝 常用Code

### 基本Scene
```javascript
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, w/h, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
```

### Load GLB Model
```javascript
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const loader = new GLTFLoader();
loader.load('MODEL_URL.glb', (gltf) => {
    const model = gltf.scene;
    scene.add(model);
});
```

### Sprite Animation
```javascript
// Use texture sprite sheet
const texture = new THREE.TextureLoader().load('spritesheet.png');
const sprite = new THREE.Sprite(material);
sprite.scale.set(1, 1, 1);
```

---

## 🎮 遊戲級Dashboard要點

1. **Loading優化** - 先用簡單形狀，等click先load詳細圖
2. **互動** - Raycaster做click detection
3. **動畫** - requestAnimationFrame loop
4. **粒子效果** - Points做氛圍

---

## 📦 安裝Three.js

```bash
# For Node.js project
npm install three

# CDN (for simple HTML)
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

---

## 🔗 相關Repo

- https://github.com/ReneTeacher/anime-office-dashboard

---

*最後更新: 2026-02-15*
