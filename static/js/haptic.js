/*
 * 触覚フィードバック (A-13)
 * モバイル端末でボタンなどをタップした際に微振動を起こす
 */
document.addEventListener('DOMContentLoaded', () => {
    // 振動を発生させたい要素のセレクタ
    const hapticTargets = 'a, button, .btn';

    document.querySelectorAll(hapticTargets).forEach(el => {
        el.addEventListener('click', () => {
            // navigator.vibrate が存在するかチェック (対応ブラウザのみ)
            if (window.navigator && window.navigator.vibrate) {
                // 軽い振動を10ミリ秒実行
                navigator.vibrate(10);
            }
        });
    });
});
