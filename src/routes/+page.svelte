<script>
	import { Alert, Button, Heading, P, Hr, Card } from 'flowbite-svelte';
</script>

<div class="text-center">
	<h1
		class="mb-4 text-4xl font-extrabold tracking-tight
		text-gray-900 dark:text-white md:text-5xl lg:text-6xl"
	>
		<span
			class="underline decoration-blue-400
			decoration-8 dark:decoration-blue-600"
		>
			News Scraper
		</span>
	</h1>

	<Hr classHr="my-8" />

	<Card href="/cards" class="m-auto mb-5">
		<p class="font-normal leading-tight text-black dark:text-gray-400">News network</p>
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Headline</h5>
	</Card>

	<Card href="/cards" class="m-auto mb-5">
		<p class="font-normal leading-tight text-black dark:text-gray-400">News network</p>
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Headline</h5>
	</Card>

	<Card href="/cards" class="m-auto mb-5">
		<p class="font-normal leading-tight text-black dark:text-gray-400">News network</p>
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Headline</h5>
	</Card>
</div>

<style></style>
