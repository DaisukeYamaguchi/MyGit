$(function(){
    $("#modal-open").click(function(){
        /* �I�[�o�[���C�̑��d�N����h�~ */
        //�{�^������A�E�g�t�H�[�J�X
        $(this).blur();
        //�V�������[�_���E�B���h�E���N�����Ȃ�
        if($("#modal-overlay")[0]) return false;
        /*****/
        
        //�I�[�o�[���C�𐶐�
        $("body").append('<div id="modal-overlay"></div>');
        $("#modal-overlay").fadeIn("fast");
        
        //�R���e���c���|�W�V���j���O
        positioningModal();
        
        //�R���e���c���t�F�[�h�C��
        $("#modal-content").fadeIn("fast");
        
        /* [#modal-overlay]�A�܂���[#modal-close]�N���b�N�� */
        $("#modal-overlay, #modal-close").unbind().click(function(){
            //[#modal-content]��[#modal-overlay]�̃t�F�[�h�A�E�g
            $("#modal-content,#modal-overlay").fadeOut("fast", function(){
            //[#modal-overlay]���폜
            $('#modal-overlay').remove();
        } ) ;
        /*****/
    } ) ;
} ) ;

//���T�C�Y���̃|�W�V���j���O
$(window).resize(positioningModal) ;

//�|�W�V���j���O�����s
function positioningModal() {
    //���(�E�B���h�E)�̕��A�������擾
    var w = $(window).width() ;
    var h = $(window).height() ;
    
    // �R���e���c(#modal-content)�̕��A�������擾
    // jQuery�̃o�[�W�����ɂ���ẮA����[{margin:true}]���w�肵�����A�s����N�����܂��B
    var cw = $("#modal-content").outerWidth({margin: true});
    var ch = $("#modal-content").outerHeight({margin: true});
    var cw = $("#modal-content").outerWidth();
    var ch = $("#modal-content").outerHeight();
    
    /** �|�W�V���j���O�����s����
     * ((w - cw)/2): ���[�_���̍��E�����񂹁B
     * ((h - ch)/2): ���[�_���̏㉺�����񂹁B
     * (w - cw): ���[�_���̉E�񂹁B
     * (h - ch): ���[�_���̉��񂹁B
     */
    $("#modal-content").css({"left": (w - cw) + "px", "top": "50px"});
    }
} ) ;
