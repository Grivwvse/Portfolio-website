
function sleep(ms){
    return new Promise((resolve) => setTimeout(resolve,ms));
 }

 //const phrases = ["code", "make beats"];
 const el = document.getElementById("typewriter");
 //let typetime = 150;
 //let deletetime
 //let fullwtime
 //let nulltime 
 let curPhraseIndex = 0;
 const writeLoop = async () => {
  while (true)
  {
    let curWord = phrases[curPhraseIndex];

    for(let i = 0; i < curWord.length; i++ )
    {
      el.innerText = curWord.substring(0,i+1);
      await sleep(typetime);
    }

    await sleep(fullwtime);

    for(let i = curWord.length; i > 0 ; i-- )
    {
      el.innerText = curWord.substring(0,i-1);
      await sleep(deletetime);
    }

    await sleep(nulltime);

    if (curPhraseIndex == phrases.length - 1)
    {
      curPhraseIndex = 0;
    }
    else
    {
      curPhraseIndex++;
    }
  }
 };

 writeLoop();