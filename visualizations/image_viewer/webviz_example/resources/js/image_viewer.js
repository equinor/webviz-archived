function image_viewer(containerId, imageData) {
    
    var selectors = Object.keys(imageData[0]).filter(item => item !=='IMAGEPATH')
    
    //Makes DOM elements for image and selectors
    function initDOM(imageid) {
        //Page and title
        d3.select('#'+containerId)
            .append('div')
            .attr('class','container')
    
        //Image
        d3.select('#'+containerId)
            .append('div')
            .attr('class','row')
            .attr('id',imageid+'_imagerow')
                .append('div')
                .attr("class","col-md-2")
                    .append('img')
                    .attr('id', imageid+'_image')
                    .attr('src', '')
                    .style('width','650px')
                    //.attr("class","img-responsive")
     
        //d3.select("#"+imageid+"_imagerow").node().appendChild(loadSvg(currentimage[0]['IMAGEPATH']))

        //Selector
        d3.select('#'+containerId)
            .append('div')
            .attr('class','row')
            .attr('class', 'col-md-6')
            .attr('id',imageid+'_selectorrow')
       
        for (var i in selectors) {
            let selectordiv = d3.select('#'+imageid+'_selectorrow')
                .append('div').attr("class","col-md-12")

            initSelector(selectors[i],  unique(imageData.map(d => d[selectors[i]] )), imageid, selectordiv)
         }
    }

    //Makes selectors
    function initSelector(selector, elements, imageid, selectordiv) {
        
        selectordiv = selectordiv
            .append('form')
            .attr('class', 'form-inline')
            .append('div')
            .attr('class', 'form-group')
        selectordiv.append('label')
            .attr('for', selector)
            .attr('class', 'form-control mx-sm-2')
            .html(selector)
        let selectorel = selectordiv
            .append('select')
            .attr("class","col-md-8 form-control")
            .attr("id",selector)
        selectorel.selectAll("option")
            .data(elements)
            .enter()
            .append("option")
            .text(function(d){return d;})
        selectorel.property('value',elements[0])
        selectorel.on('change', function() {changeImage(imageid)})

    }

    //Updates the image
    function changeImage(imageid){
        var currentselection = []
        var currentimage = imageData
        for (var i in selectors) {

            currentselection[i] = d3.select('#' + selectors[i]).property('value')
            currentimage = currentimage.filter(function(d){return (String(currentselection[i]).includes(d[selectors[i]]));});
        }
        if (Array.isArray(currentimage)) {
            if (currentimage[0].hasOwnProperty('IMAGEPATH')) {
                d3.select('#'+imageid+'_image').attr('src', currentimage[0]['IMAGEPATH'])            
            }
            else { d3.select('#'+imageid+'_image').attr('src', '')   }
        }
        else { d3.select('#'+imageid+'_image').attr('src', '')   }
        //d3.select("#"+imageid+"_imagerow").selectAll('svg').remove()
        //d3.select("#"+imageid+"_imagerow").node().appendChild(loadSvg(currentimage[0]['IMAGEPATH']))
    }
    
    //Loads a SVG from file/url
    function loadSvg(path) {
        d3.xml(path).mimeType("image/svg+xml").get(function(error, xml) {
            if (error) throw error;
            return xml.documentElement      
        })
    }
    function unique(x) {
    //Function that returns unique elements in a list.
    //Used to find selectors
        return x.reverse().filter(function (e, i, x) {return x.indexOf(e, i+1) === -1;}).reverse();
    }

    initDOM('image0')
    changeImage('image0')
    

}