
        //This function powers the next and back buttons showing the various questions
        function style(from, to) {
            document.getElementById(from).style.display = "none";
            document.getElementById(to).style.cssText += ';display:block;'
        }

            function changeview(e){
                if (e.target !== e.currentTarget && !(e.target.type == "radio")) {
                    var clickedItem = e.target.id;
                    var buttonType = $('#' + clickedItem).data();
                    var ischecked = false;
                    function checkradios(buttonType) {
                        var howmanychecked = []
                        var labelGroups = document.getElementById("questionForm").getElementsByTagName('label');
                        for (var i = 0; i < labelGroups.length; i++) {
                            var code = labelGroups[i].htmlFor;
                            var chx = document.getElementsByName(code);
                            for (var t = 0; t < chx.length; t++) {
                                if (chx[t].type == 'radio' && chx[t].checked) {
                                    howmanychecked.push(t);
                                }
                            }
                        }
                        //Round off the right end of the progress bar when all questions are complete
                        if (howmanychecked.length > 9) {
                            document.getElementById("progressSpan").style.borderTopRightRadius = "8px";
                            document.getElementById("progressSpan").style.borderBottomRightRadius = "8px";
                            document.getElementById("progressBar").style.display = "none";
                        }
                        //If user backs up to the start of the quiz the button should say "resume quiz" rather than "start quiz"
                        if (howmanychecked.length > 0) {
                            document.getElementById("startquizbutton").innerHTML = "Resume quiz"
                        }
                        //The following two lines lengthen the progress bar and set its text
                        document.getElementById("progressSpan").style.width = howmanychecked.length * 10 + "%";
                        document.getElementById("progressSpan").innerHTML = howmanychecked.length * 10 + "%";
                        var questionCode = document.getElementById(buttonType.next).parentNode.getElementsByTagName('label')[0].htmlFor;
                        var chx = document.getElementsByName(questionCode);
                        for (var i = 0; i < chx.length; i++) {
                            if (chx[i].type == 'radio' && chx[i].checked && chx[i].name == questionCode) {
                                ischecked = true;
                                return true
                            }
                        }                       
                    }
                    if (buttonType.next && !(buttonType.next == "questionblock9")) {
                        checkradios(buttonType);
                        if (ischecked == false) {
                            alert("You have to check an answer before you can proceed!")
                        } else {
                            var thisBlock = buttonType.next;
                            var nextBlock = thisBlock.replace(thisBlock.slice(-1), (parseInt(thisBlock.slice(-1)) + 1).toString());
                            style(thisBlock, nextBlock);
                        };                       
                    } else if (buttonType.next && buttonType.next == "questionblock9") {
                        checkradios(buttonType)
                        if (ischecked == false) {
                            alert("You have to check an answer before you can proceed!")
                        } else {
                            style("questionblock9", "submitPanel");
                            document.getElementById("lastp").style.display = "block";
                        };                       
                    }else if (buttonType.back && !(buttonType.back == "questionblock0")) {
                        var thisBlock = buttonType.back;
                        var nextBlock = thisBlock.replace(thisBlock.slice(-1), (parseInt(thisBlock.slice(-1)) - 1).toString());
                        style(thisBlock, nextBlock);
                    } else if (buttonType.back && buttonType.back == "questionblock0") {
                        document.getElementById("progressBar").style.display = "none";
                        style("questionblock0", "startquiz");
                    } else if (buttonType.final) {
                        
                        style("submitPanel", "questionblock9");
                    } 
                }
                e.stopPropagation();
            }
            $("#questionForm").click(changeview)

            document.getElementById('startquizbutton').onclick = function (e) {
                style("startquiz", "questionblock0")
                document.getElementById("buttonholder").style.display = "block";
                document.getElementById("progressBar").style.display = "block";
            }
