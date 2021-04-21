window.onload=function(){window.jQuery?$(document).ready(function(){$(".sidebarNavigation .navbar-collapse").hide().clone().appendTo("body").removeAttr("class").addClass("sideMenu").show(),$("body").append("<div class='overlay'></div>"),$(".navbar-toggle").on("click",function(){$(".sideMenu").addClass($(".sidebarNavigation").attr("data-sidebarClass")),$(".sideMenu, .overlay").toggleClass("open"),$(".overlay").on("click",function(){$(this).removeClass("open"),$(".sideMenu").removeClass("open")})}),$(window).resize(function(){$(".navbar-toggle").is(":hidden")?$(".sideMenu, .overlay").hide():$(".sideMenu, .overlay").show()})}):console.log("sidebarNavigation Requires jQuery")};

$(document).ready(function() {

  $(".toggle-accordion").on("click", function() {
    var accordionId = $(this).attr("accordion-id"),
      numPanelOpen = $(accordionId + ' .collapse.in').length;
    
    $(this).toggleClass("active");

    if (numPanelOpen == 0) {
      openAllPanels(accordionId);
    } else {
      closeAllPanels(accordionId);
    }
  })

  // openAllPanels = function(aId) {
  //   console.log("setAllPanelOpen");
  //   $(aId + ' .panel-collapse:not(".in")').collapse('show');
  // }
  // closeAllPanels = function(aId) {
  //   console.log("setAllPanelclose");
  //   $(aId + ' .panel-collapse.in').collapse('hide');
  // }
     
});

<script>
window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
</script>