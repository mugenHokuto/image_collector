import streamlit as st
import os
from pathlib import Path
from icrawler.builtin import BingImageCrawler

# ページ設定
st.set_page_config(
    page_title="画像収集ソフト",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ 画像収集ソフト")
st.markdown("キーワードを入力して画像を収集します")

# サイドバーに設定項目
with st.sidebar:
    st.header("設定")
    
    keyword = st.text_input(
        "検索キーワード",
        value="cute cat",
        help="収集したい画像のキーワードを入力してください"
    )
    
    folder_name = st.text_input(
        "保存先フォルダ名",
        value="imageGetter",
        help="画像を保存するフォルダ名を入力してください（相対パスまたは絶対パス）。例: imageGetter または C:\\Users\\...\\imageGetter"
    )
    
    max_num = st.number_input(
        "最大画像数",
        min_value=1,
        max_value=1000,
        value=100,
        step=1,
        help="収集する画像の最大数を指定してください"
    )
    
    st.subheader("画像サイズ設定")
    min_size_enabled = st.checkbox("最小サイズを指定する", value=True)
    
    if min_size_enabled:
        col1, col2 = st.columns(2)
        with col1:
            min_width = st.number_input("最小幅", min_value=1, value=200, step=10)
        with col2:
            min_height = st.number_input("最小高さ", min_value=1, value=200, step=10)
        min_size = (min_width, min_height)
    else:
        min_size = None
    
    start_button = st.button("📥 画像収集を開始", type="primary", use_container_width=True)

# メインエリア
if start_button:
    if not keyword:
        st.error("❌ キーワードを入力してください")
    elif not folder_name:
        st.error("❌ 保存先フォルダ名を入力してください")
    else:
        try:
            # 進捗バー
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("🔄 画像収集を開始しています...")
            progress_bar.progress(10)
            
            # フォルダの作成
            os.makedirs(folder_name, exist_ok=True)
            status_text.text(f"📁 フォルダ '{folder_name}' を作成しました")
            progress_bar.progress(30)
            
            # 画像収集の実行
            status_text.text(f"🔍 キーワード '{keyword}' で画像を検索中...")
            progress_bar.progress(50)
            
            crawler = BingImageCrawler(storage={'root_dir': folder_name})
            
            if min_size:
                crawler.crawl(keyword=keyword, max_num=max_num, min_size=min_size)
            else:
                crawler.crawl(keyword=keyword, max_num=max_num)
            
            progress_bar.progress(90)
            status_text.text("✅ 画像収集が完了しました！")
            progress_bar.progress(100)
            
            # 結果の表示
            saved_folder = Path(folder_name)
            if saved_folder.exists():
                image_files = list(saved_folder.glob("*.jpg")) + list(saved_folder.glob("*.png"))
                image_count = len(image_files)
                
                st.success(f"✅ {image_count}枚の画像を収集しました！")
                st.info(f"📁 保存先: `{folder_name}`")
                
                # 収集した画像のプレビュー（最初の9枚）
                if image_count > 0:
                    st.subheader("📸 収集した画像のプレビュー")
                    cols = st.columns(3)
                    for idx, img_path in enumerate(image_files[:9]):
                        with cols[idx % 3]:
                            st.image(str(img_path), caption=img_path.name, use_container_width=True)
        except Exception as e:
            st.error(f"❌ エラーが発生しました: {str(e)}")
            st.exception(e)

# 使い方の説明
with st.expander("📖 使い方"):
    st.markdown("""
    ### 使い方
    
    1. **キーワード入力**: 収集したい画像のキーワードを入力します
    2. **保存先フォルダ名**: 画像を保存するフォルダ名を指定します
    3. **最大画像数**: 収集する画像の最大数を設定します
    4. **最小サイズ設定**: 画像の最小サイズを指定できます（オプション）
    5. **画像収集を開始**: ボタンをクリックして収集を開始します
    
    ### 注意事項
    
    - 画像の収集には時間がかかる場合があります
    - インターネット接続が必要です
    - 収集した画像の著作権にご注意ください
    """)

