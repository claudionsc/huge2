/**
 * ALVI - Advanced 3D Interactive Experience
 * 
 * Features:
 * 1. Carbon-Fiber Micro-Triangular Sphere:
 *    - Extremely high geometry density (Icosahedron detail 7 = 327,680 micro-triangles + micro-weave procedural enhancement).
 *    - Transparent body with visible wireframe mesh.
 *    - Fine graphite and silver wireframe lines with subtle specular reflections & Fresnel rim.
 * 2. Permanent Smooth Wave Background:
 *    - Deep graphite organic waves generated procedurally on GPU via GLSL from scroll = 0 (Home/Hero).
 *    - Always present in the background, continuously moving.
 * 3. Optical Lens Distortion (Geometric Fisheye/Barrel Deformation):
 *    - True radial lens deformation curving the edges and corners as the sphere expands.
 * 4. Powerful Chromatic Aberration:
 *    - Pronounced RGB channel separation (15-30px in corners).
 *    - Radial non-linear falloff (clean center, intense at extremities).
 *    - Stays actively engaged in the final background.
 * 5. Unified Normalized Scroll Synchronization.
 */

(function () {
    'use strict';

    // --- Configuration Controls ---
    const CONFIG = {
        // Geometry
        sphereRadius: 1.30,         // Compact initial sphere size
        subdivisionDetail: 7,       // Level 7 = 327,680 micro-triangles (4x detail 6, next geodesic subdivision)
        
        // Colors & Lighting
        bodyColor: [0.002, 0.002, 0.003],    // Pure matte black body (zero specular reflections)
        lineBaseColor: [0.12, 0.13, 0.15],   // Dark graphite base line
        lineGleamColor: [0.72, 0.76, 0.82],  // Subtle silver/platinum highlight on lines
        
        // Chromatic Aberration & Lens Distortion
        aberrationBase: 0.038,      // Visible chromatic aberration at corners from scroll = 0
        aberrationMax: 0.085,       // Maximum chromatic aberration (15-30px separation at corners)
        distortionBase: 0.08,       // Subtle initial optical lens curve
        distortionMax: 0.38,        // Strong radial distortion at corners when expanded
        
        // Blur & Wave Blend
        blurMax: 0.65,              // Softens micro-grid at Services for optimal text contrast
        waveSpeed: 0.55             // Speed of procedural wavefield
    };

    function isWebGLAvailable() {
        try {
            const canvas = document.createElement('canvas');
            return !!(window.WebGLRenderingContext && (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
        } catch (e) {
            return false;
        }
    }

    if (!isWebGLAvailable() || typeof THREE === 'undefined') {
        console.warn('WebGL or Three.js unavailable - 3D experience skipped.');
        return;
    }

    const canvas = document.getElementById('webgl-sphere');
    if (!canvas) return;

    // --- Renderer Setup ---
    const renderer = new THREE.WebGLRenderer({
        canvas: canvas,
        alpha: true,
        antialias: true,
        powerPreference: 'high-performance'
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // --- 3D Scene & Perspective Camera ---
    const scene3D = new THREE.Scene();
    const camera3D = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera3D.position.set(0, 0, 5.5);

    // --- High-Density Carbon-Fiber Sphere Geometry ---
    // Icosahedron detail 7 = 20 * 4^7 = 327,680 micro-triangles, 983,040 vertices
    const baseGeom = new THREE.IcosahedronGeometry(CONFIG.sphereRadius, CONFIG.subdivisionDetail);
    const nonIndexedGeom = baseGeom.toNonIndexed();

    const vertexCount = nonIndexedGeom.attributes.position.count;
    const posAttr = nonIndexedGeom.attributes.position;
    const origPosArray = new Float32Array(vertexCount * 3);
    const barycentricArray = new Float32Array(vertexCount * 3);

    for (let i = 0; i < vertexCount; i++) {
        const x = posAttr.getX(i);
        const y = posAttr.getY(i);
        const z = posAttr.getZ(i);
        const len = Math.sqrt(x * x + y * y + z * z) || 1.0;
        origPosArray[i * 3 + 0] = x / len;
        origPosArray[i * 3 + 1] = y / len;
        origPosArray[i * 3 + 2] = z / len;

        const corner = i % 3;
        barycentricArray[i * 3 + 0] = corner === 0 ? 1 : 0;
        barycentricArray[i * 3 + 1] = corner === 1 ? 1 : 0;
        barycentricArray[i * 3 + 2] = corner === 2 ? 1 : 0;
    }

    nonIndexedGeom.setAttribute('aOrigPos', new THREE.BufferAttribute(origPosArray, 3));
    nonIndexedGeom.setAttribute('aBarycentric', new THREE.BufferAttribute(barycentricArray, 3));

    // --- 3D Carbon Fiber Sphere Material ---
    const sphereMaterial = new THREE.ShaderMaterial({
        uniforms: {
            uProgress: { value: 0.0 },
            uTime: { value: 0.0 },
            uMouse: { value: new THREE.Vector2(0, 0) },
            uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
            uKeyLightPos: { value: new THREE.Vector3(4.0, 4.5, 5.0) },
            uFillLightPos: { value: new THREE.Vector3(-4.0, -3.0, 2.5) }
        },
        vertexShader: `
            attribute vec3 aOrigPos;
            attribute vec3 aBarycentric;

            varying vec3 vWorldPos;
            varying vec3 vOrigPos;
            varying vec3 vBarycentric;
            varying float vProgress;

            uniform float uProgress;
            uniform float uTime;
            uniform vec2 uMouse;
            uniform vec2 uResolution;

            void main() {
                vOrigPos = aOrigPos;
                vBarycentric = aBarycentric;
                vProgress = uProgress;

                // Slow rotation + mouse parallax
                float rotSpeed = mix(0.065, 0.015, uProgress);
                float rotY = uTime * rotSpeed + uMouse.x * mix(0.28, 0.06, uProgress);
                float rotX = -0.10 + uMouse.y * mix(0.20, 0.04, uProgress);

                mat3 rotMatY = mat3(
                    cos(rotY), 0.0, sin(rotY),
                    0.0, 1.0, 0.0,
                    -sin(rotY), 0.0, cos(rotY)
                );
                mat3 rotMatX = mat3(
                    1.0, 0.0, 0.0,
                    0.0, cos(rotX), -sin(rotX),
                    0.0, sin(rotX), cos(rotX)
                );
                vec3 pRot = rotMatX * rotMatY * aOrigPos;

                float aspect = uResolution.x / uResolution.y;
                float halfH = 5.5 * tan(radians(22.5));
                float halfW = halfH * aspect;
                float maxHalf = max(halfW, halfH);

                float k = smoothstep(0.0, 1.0, uProgress);
                float scale = mix(1.30, 5.8, k);

                // Flattening target: mesh extends past viewport edges
                float xFlat = pRot.x * maxHalf * 1.65;
                float yFlat = pRot.y * maxHalf * 1.65;
                float zRelief = 0.12 + sin(pRot.x * 6.0 + uTime * 0.35) * 0.06 + cos(pRot.y * 6.0) * 0.06;

                vec3 finalPos;
                if (pRot.z >= -0.15) {
                    vec3 spherePos = pRot * scale;
                    vec3 flatPos = vec3(xFlat, yFlat, zRelief);
                    finalPos = mix(spherePos, flatPos, pow(k, 1.15));
                } else {
                    vec3 spherePos = pRot * scale;
                    vec3 backPos = vec3(pRot.x * scale * 1.2, pRot.y * scale * 1.2, pRot.z * scale - k * 3.5);
                    finalPos = mix(spherePos, backPos, k);
                }

                vWorldPos = finalPos;
                gl_Position = projectionMatrix * modelViewMatrix * vec4(finalPos, 1.0);
            }
        `,
        fragmentShader: `
            varying vec3 vWorldPos;
            varying vec3 vOrigPos;
            varying vec3 vBarycentric;
            varying float vProgress;

            uniform vec3 uKeyLightPos;
            uniform vec3 uFillLightPos;
            uniform float uTime;

            void main() {
                // Fade back hemisphere when expanding
                if (vOrigPos.z < -0.15 && vProgress > 0.45) {
                    float fade = 1.0 - smoothstep(0.45, 0.80, vProgress);
                    if (fade < 0.02) discard;
                }

                // True flat normal of the micro-facet
                vec3 fNormal = normalize(cross(dFdx(vWorldPos), dFdy(vWorldPos)));
                vec3 viewDir = normalize(vec3(0.0, 0.0, 5.5) - vWorldPos);

                // Key Light
                vec3 keyDir = normalize(uKeyLightPos - vWorldPos);
                vec3 keyHalf = normalize(keyDir + viewDir);
                float keySpec = pow(max(dot(fNormal, keyHalf), 0.0), 32.0);

                // Fill Light
                vec3 fillDir = normalize(uFillLightPos - vWorldPos);
                float fillDiff = max(dot(fNormal, fillDir), 0.0);

                // Fresnel
                float fresnel = pow(1.0 - max(dot(fNormal, viewDir), 0.0), 3.0);

                // Transparent face: nearly invisible, only wireframe visible
                vec3 faceColor = vec3(0.003, 0.003, 0.004);
                float faceAlpha = 0.04;  // Nearly transparent faces

                // Wireframe Edge Detection via Barycentric Coordinates
                vec3 dBary = fwidth(vBarycentric);
                vec3 a3 = smoothstep(vec3(0.0), dBary * 1.35, vBarycentric);
                float edgeFactor = 1.0 - min(min(a3.x, a3.y), a3.z);

                // Wireframe Lines: Graphite and Silver with subtle gleam
                vec3 lineBase = vec3(0.11, 0.12, 0.14);
                vec3 lineGleam = vec3(0.68, 0.72, 0.78);
                float lineGleamIntensity = keySpec * 1.4 + fresnel * 0.45 + fillDiff * 0.15;
                vec3 lineColor = mix(lineBase, lineGleam, clamp(lineGleamIntensity, 0.0, 1.0));
                float lineAlpha = mix(0.75, 0.55, vProgress);  // Visible wireframe lines

                // Blend face and line colors with their respective alphas
                vec3 finalColor = mix(faceColor, lineColor, edgeFactor * 0.90);
                float alpha = mix(faceAlpha, lineAlpha, edgeFactor * 0.90);

                gl_FragColor = vec4(finalColor, alpha);
            }
        `,
        transparent: true,
        side: THREE.DoubleSide,
        depthWrite: false,
        depthTest: true,
        blending: THREE.NormalBlending
    });

    const sphereMesh = new THREE.Mesh(nonIndexedGeom, sphereMaterial);
    scene3D.add(sphereMesh);

    // --- Cinematic Ambient Particles ---
    const PARTICLE_COUNT = 340;
    const particleGeom = new THREE.BufferGeometry();
    const particlePositions = new Float32Array(PARTICLE_COUNT * 3);
    const particleVelocities = new Float32Array(PARTICLE_COUNT * 3);

    for (let i = 0; i < PARTICLE_COUNT; i++) {
        const u = Math.random();
        const v = Math.random();
        const theta = u * 2.0 * Math.PI;
        const phi = Math.acos(2.0 * v - 1.0);
        const r = 1.8 + Math.random() * 4.2;

        particlePositions[i * 3 + 0] = r * Math.sin(phi) * Math.cos(theta);
        particlePositions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
        particlePositions[i * 3 + 2] = (r * Math.cos(phi)) * 0.8;

        particleVelocities[i * 3 + 0] = (Math.random() - 0.5) * 0.0025;
        particleVelocities[i * 3 + 1] = (Math.random() - 0.5) * 0.0025;
        particleVelocities[i * 3 + 2] = (Math.random() - 0.5) * 0.0018;
    }

    particleGeom.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));

    function createParticleTexture() {
        const c = document.createElement('canvas');
        c.width = 32;
        c.height = 32;
        const ctx = c.getContext('2d');
        const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
        grad.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
        grad.addColorStop(0.35, 'rgba(200, 215, 235, 0.5)');
        grad.addColorStop(0.7, 'rgba(160, 180, 205, 0.15)');
        grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, 32, 32);
        return new THREE.CanvasTexture(c);
    }

    const particleMaterial = new THREE.PointsMaterial({
        size: 0.052,
        map: createParticleTexture(),
        transparent: true,
        opacity: 0.28,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    const particles = new THREE.Points(particleGeom, particleMaterial);
    scene3D.add(particles);

    // --- Offscreen Render Target for 3D Scene ---
    let renderTarget = new THREE.WebGLRenderTarget(window.innerWidth, window.innerHeight, {
        minFilter: THREE.LinearFilter,
        magFilter: THREE.LinearFilter,
        format: THREE.RGBAFormat
    });

    // --- Fullscreen Compositing Scene: Wavefield + Optical Distortion + Chromatic Aberration ---
    const postScene = new THREE.Scene();
    const postCamera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

    const postMaterial = new THREE.ShaderMaterial({
        uniforms: {
            tScene: { value: renderTarget.texture },
            uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) },
            uTime: { value: 0.0 },
            uProgress: { value: 0.0 },
            uBlur: { value: 0.0 },
            uAberration: { value: CONFIG.aberrationBase },
            uDistortion: { value: CONFIG.distortionBase },
            uMeshMix: { value: 1.0 }
        },
        vertexShader: `
            varying vec2 vUv;
            void main() {
                vUv = uv;
                gl_Position = vec4(position, 1.0);
            }
        `,
        fragmentShader: `
            precision highp float;

            varying vec2 vUv;
            uniform sampler2D tScene;
            uniform vec2 uResolution;
            uniform float uTime;
            uniform float uProgress;
            uniform float uBlur;
            uniform float uAberration;
            uniform float uDistortion;
            uniform float uMeshMix;

            // --- Multi-tap Gaussian Blur on Scene Texture ---
            vec4 getBlurredScene(vec2 uv, float blurAmount) {
                if (blurAmount < 0.005) {
                    return texture2D(tScene, uv);
                }

                vec4 col = vec4(0.0);
                float totalWeight = 0.0;
                vec2 aspectCorrection = vec2(uResolution.y / uResolution.x, 1.0);
                vec2 radius = aspectCorrection * (blurAmount * 0.015);

                col += texture2D(tScene, uv) * 0.22;
                totalWeight += 0.22;

                vec2 o1 = radius * 0.55;
                col += texture2D(tScene, uv + vec2(o1.x, 0.0)) * 0.12;
                col += texture2D(tScene, uv - vec2(o1.x, 0.0)) * 0.12;
                col += texture2D(tScene, uv + vec2(0.0, o1.y)) * 0.12;
                col += texture2D(tScene, uv - vec2(0.0, o1.y)) * 0.12;
                totalWeight += 0.48;

                vec2 o2 = radius * 0.95;
                col += texture2D(tScene, uv + vec2(o2.x, o2.y)) * 0.075;
                col += texture2D(tScene, uv + vec2(-o2.x, o2.y)) * 0.075;
                col += texture2D(tScene, uv + vec2(o2.x, -o2.y)) * 0.075;
                col += texture2D(tScene, uv + vec2(-o2.x, -o2.y)) * 0.075;
                totalWeight += 0.30;

                return col / totalWeight;
            }

            // --- Procedural Dark Graphite Wave Heightfield ---
            float waveHeight(vec2 p, float time) {
                vec2 q = vec2(
                    sin(p.x * 1.5 + time * 0.20) + cos(p.y * 1.3 - time * 0.16),
                    cos(p.x * 1.2 - time * 0.17) + sin(p.y * 1.6 + time * 0.22)
                );

                vec2 r = p + 0.32 * q;

                float h1 = sin(r.x * 2.0 + r.y * 1.2 + time * 0.24) * 0.5 + 0.5;
                float h2 = cos(r.x * 3.2 - r.y * 2.0 - time * 0.30) * 0.25;
                float h3 = sin(r.x * 5.4 + r.y * 4.2 + time * 0.36) * 0.12;

                return h1 + h2 + h3;
            }

            // --- Calculate Wave Shading at UV ---
            vec3 getWaveColor(vec2 uv, float time) {
                vec2 uvScaled = (uv - 0.5) * vec2(uResolution.x / uResolution.y, 1.0) * 3.4;
                vec2 eps = vec2(0.016, 0.0);
                float hC = waveHeight(uvScaled, time);
                float hR = waveHeight(uvScaled + eps.xy, time);
                float hU = waveHeight(uvScaled + eps.yx, time);

                vec3 waveNormal = normalize(vec3((hC - hR) * 2.4, (hC - hU) * 2.4, 0.16));

                vec3 lightDir1 = normalize(vec3(0.55, 0.75, 0.85));
                vec3 lightDir2 = normalize(vec3(-0.65, -0.45, 0.50));
                vec3 viewDir = vec3(0.0, 0.0, 1.0);

                float diff1 = max(dot(waveNormal, lightDir1), 0.0);
                float diff2 = max(dot(waveNormal, lightDir2), 0.0);
                float spec = pow(max(dot(reflect(-lightDir1, waveNormal), viewDir), 0.0), 20.0);
                float fresnel = pow(1.0 - max(dot(waveNormal, viewDir), 0.0), 2.8);

                // Deep graphite & black tones
                vec3 waveBase = vec3(0.012, 0.013, 0.016);
                vec3 waveHighlight = vec3(0.052, 0.058, 0.068);
                vec3 waveSheen = vec3(0.18, 0.20, 0.24);

                return waveBase 
                     + waveHighlight * (diff1 * 0.75 + diff2 * 0.25) 
                     + waveSheen * (spec * 0.40 + fresnel * 0.30);
            }

            void main() {
                vec2 uv = vUv;
                vec2 p = uv - 0.5;
                vec2 pAspect = p * vec2(uResolution.x / uResolution.y, 1.0);
                float r2 = dot(pAspect, pAspect); // 0 at center, ~0.65 at edges, ~0.95 at corners

                // --- 1. Real Geometric Lens Distortion (Barrel/Fisheye Deformation) ---
                // Deforms the image coordinates radially toward the edges/corners
                float distFactor = 1.0 + uDistortion * r2 * (1.0 + 0.6 * r2);
                vec2 pDistorted = p * distFactor;
                vec2 uvDistorted = 0.5 + pDistorted;

                // --- 2. Powerful Chromatic Aberration (15-30px RGB Separation at Corners) ---
                // Non-linear radial curve: clean center, dramatic separation at corners
                float caStrength = uAberration * pow(r2 * 1.5, 2.0);
                vec2 dir = normalize(pAspect + 0.0001);

                vec2 uvR = 0.5 + (pDistorted + dir * caStrength * 0.60);
                vec2 uvG = 0.5 + pDistorted;
                vec2 uvB = 0.5 + (pDistorted - dir * caStrength * 0.60);

                // --- 3. Sample 3D Sphere Scene with Distortion & Aberration ---
                float sceneR = getBlurredScene(uvR, uBlur).r;
                float sceneG = getBlurredScene(uvG, uBlur).g;
                float sceneB = getBlurredScene(uvB, uBlur).b;
                float sceneA = getBlurredScene(uvDistorted, uBlur).a;
                vec3 sceneColor = vec3(sceneR, sceneG, sceneB);

                // --- 4. Render Permanent Smooth Wave Background (Present from Scroll = 0) ---
                float waveTime = uTime * 0.55;
                vec3 waveColorR = getWaveColor(uvR, waveTime);
                vec3 waveColorG = getWaveColor(uvG, waveTime);
                vec3 waveColorB = getWaveColor(uvB, waveTime);
                vec3 waveColor = vec3(waveColorR.r, waveColorG.g, waveColorB.b);

                // Edge chromatic glow on waves in corners
                float cornerGlow = pow(r2 * 1.3, 2.8) * uAberration;
                waveColor.r += cornerGlow * 0.12;
                waveColor.b += cornerGlow * 0.16;

                // --- 5. Composite Sphere over Permanent Wave Background ---
                // At scroll = 0: Sphere sits over waves with alpha blending
                // As sphere expands: micro-triangular pattern weaves into the wave texture
                vec3 finalComposite;
                if (uProgress < 0.45) {
                    finalComposite = mix(waveColor, sceneColor, sceneA);
                } else {
                    // Transition to integrated geometric background:
                    // Both the micro-triangles and the wave field remain active together!
                    vec3 integratedMesh = waveColor + sceneColor * 0.85;
                    float blendK = smoothstep(0.45, 0.85, uProgress);
                    finalComposite = mix(mix(waveColor, sceneColor, sceneA), integratedMesh, blendK);
                }

                gl_FragColor = vec4(finalComposite, 1.0);
            }
        `,
        transparent: false
    });

    const postQuad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), postMaterial);
    postScene.add(postQuad);

    // --- Unified Normalized Experience Control ---
    let targetProgress = 0.0;
    let currentProgress = 0.0;
    let targetBlur = 0.0;
    let currentBlur = 0.0;
    let targetAberration = CONFIG.aberrationBase;
    let currentAberration = CONFIG.aberrationBase;
    let targetDistortion = CONFIG.distortionBase;
    let currentDistortion = CONFIG.distortionBase;

    let targetMouseX = 0.0;
    let targetMouseY = 0.0;
    let currentMouseX = 0.0;
    let currentMouseY = 0.0;

    function onScroll() {
        const scrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
        const vh = window.innerHeight;

        const servicesEl = document.getElementById('services');
        const servicesTop = servicesEl ? servicesEl.offsetTop : vh * 2.0;

        // 1. Sphere Scale & Expansion
        const expandEnd = servicesTop * 0.90;
        targetProgress = Math.min(Math.max(scrollY / expandEnd, 0.0), 1.0);

        // 2. Powerful Chromatic Aberration: starts at aberrationBase, scales to aberrationMax, STAYS at max
        const caEnd = servicesTop * 1.0;
        const caT = Math.min(Math.max(scrollY / caEnd, 0.0), 1.0);
        targetAberration = CONFIG.aberrationBase + (CONFIG.aberrationMax - CONFIG.aberrationBase) * caT;

        // 3. Real Geometric Distortion (Barrel/Fisheye): increases as sphere expands, STAYS in background
        targetDistortion = CONFIG.distortionBase + (CONFIG.distortionMax - CONFIG.distortionBase) * caT;

        // 4. Progressive Blur: begins as user approaches Services section
        const blurStart = servicesTop - vh * 0.70;
        const blurEnd = servicesTop + vh * 0.30;
        targetBlur = Math.min(Math.max((scrollY - blurStart) / (blurEnd - blurStart), 0.0), CONFIG.blurMax);
    }

    function onMouseMove(e) {
        targetMouseX = (e.clientX / window.innerWidth) * 2 - 1;
        targetMouseY = -(e.clientY / window.innerHeight) * 2 + 1;
    }

    function onResize() {
        const w = window.innerWidth;
        const h = window.innerHeight;

        camera3D.aspect = w / h;
        camera3D.updateProjectionMatrix();

        renderer.setSize(w, h);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        renderTarget.setSize(w, h);

        sphereMaterial.uniforms.uResolution.value.set(w, h);
        postMaterial.uniforms.uResolution.value.set(w, h);

        onScroll();
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('mousemove', onMouseMove, { passive: true });
    window.addEventListener('resize', onResize, { passive: true });

    onScroll();

    // --- Main Animation Loop ---
    const clock = new THREE.Clock();
    let isVisible = true;

    document.addEventListener('visibilitychange', () => {
        isVisible = !document.hidden;
    });

    function animate() {
        requestAnimationFrame(animate);
        if (!isVisible) return;

        const elapsedTime = clock.getElapsedTime();

        // Smooth damping
        currentProgress += (targetProgress - currentProgress) * 0.055;
        currentBlur += (targetBlur - currentBlur) * 0.055;
        currentAberration += (targetAberration - currentAberration) * 0.055;
        currentDistortion += (targetDistortion - currentDistortion) * 0.055;

        currentMouseX += (targetMouseX - currentMouseX) * 0.045;
        currentMouseY += (targetMouseY - currentMouseY) * 0.045;

        // Update 3D Sphere Uniforms
        sphereMaterial.uniforms.uTime.value = elapsedTime;
        sphereMaterial.uniforms.uProgress.value = currentProgress;
        sphereMaterial.uniforms.uMouse.value.set(currentMouseX, currentMouseY);

        // Animate Ambient Particles
        const pPos = particleGeom.attributes.position.array;
        for (let i = 0; i < PARTICLE_COUNT; i++) {
            pPos[i * 3 + 0] += particleVelocities[i * 3 + 0];
            pPos[i * 3 + 1] += particleVelocities[i * 3 + 1];
            pPos[i * 3 + 2] += particleVelocities[i * 3 + 2];

            const expand = 1.0 + currentProgress * 0.35;
            const d = Math.sqrt(pPos[i * 3] * pPos[i * 3] + pPos[i * 3 + 1] * pPos[i * 3 + 1]);
            if (d > 6.5 * expand) {
                pPos[i * 3 + 0] *= 0.5;
                pPos[i * 3 + 1] *= 0.5;
            }
        }
        particleGeom.attributes.position.needsUpdate = true;
        particles.rotation.y = elapsedTime * 0.018 + currentProgress * 0.15;

        // Pass 1: Render 3D Sphere & Particles Scene to Offscreen Render Target
        renderer.setRenderTarget(renderTarget);
        renderer.clear();
        renderer.render(scene3D, camera3D);

        // Pass 2: Render Permanent Wave Background + Geometric Mesh + Lens Distortion + Strong Chromatic Aberration
        renderer.setRenderTarget(null);
        postMaterial.uniforms.uTime.value = elapsedTime;
        postMaterial.uniforms.uProgress.value = currentProgress;
        postMaterial.uniforms.uBlur.value = currentBlur;
        postMaterial.uniforms.uAberration.value = currentAberration;
        postMaterial.uniforms.uDistortion.value = currentDistortion;

        renderer.render(postScene, postCamera);
    }

    animate();
})();
