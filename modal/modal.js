$(function(){
    $("#modal-open").click(function(){
        /* オーバーレイの多重起動を防止 */
        //ボタンからアウトフォーカス
        $(this).blur();
        //新しくモーダルウィンドウを起動しない
        if($("#modal-overlay")[0]) return false;
        /*****/
        
        //オーバーレイを生成
        $("body").append('<div id="modal-overlay"></div>');
        $("#modal-overlay").fadeIn("fast");
        
        //コンテンツをポジショニング
        positioningModal();
        
        //コンテンツをフェードイン
        $("#modal-content").fadeIn("fast");
        
        /* [#modal-overlay]、または[#modal-close]クリック時 */
        $("#modal-overlay, #modal-close").unbind().click(function(){
            //[#modal-content]と[#modal-overlay]のフェードアウト
            $("#modal-content,#modal-overlay").fadeOut("fast", function(){
            //[#modal-overlay]を削除
            $('#modal-overlay').remove();
        } ) ;
        /*****/
    } ) ;
} ) ;

//リサイズ時のポジショニング
$(window).resize(positioningModal) ;

//ポジショニングを実行
function positioningModal() {
    //画面(ウィンドウ)の幅、高さを取得
    var w = $(window).width() ;
    var h = $(window).height() ;
    
    // コンテンツ(#modal-content)の幅、高さを取得
    // jQueryのバージョンによっては、引数[{margin:true}]を指定した時、不具合を起こします。
    var cw = $("#modal-content").outerWidth({margin: true});
    var ch = $("#modal-content").outerHeight({margin: true});
    var cw = $("#modal-content").outerWidth();
    var ch = $("#modal-content").outerHeight();
    
    /** ポジショニングを実行する
     * ((w - cw)/2): モーダルの左右中央寄せ。
     * ((h - ch)/2): モーダルの上下中央寄せ。
     * (w - cw): モーダルの右寄せ。
     * (h - ch): モーダルの下寄せ。
     */
    $("#modal-content").css({"left": (w - cw) + "px", "top": "50px"});
    }
} ) ;
