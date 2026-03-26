from django.core.management.base import BaseCommand
from core.models import Pet


class Command(BaseCommand):
    help = 'Seed the database with sample pet data'

    def handle(self, *args, **options):
        if Pet.objects.exists():
            self.stdout.write(self.style.WARNING('Pets already exist. Skipping seed.'))
            return

        cats = [
            {
                'name': 'Luna',
                'species': 'cat',
                'breed': 'Persian',
                'age': '2 years',
                'gender': 'female',
                'description': 'Luna is a beautiful, fluffy Persian cat with striking blue eyes. She loves lounging in sunny spots and being gently brushed. She is calm, affectionate, and enjoys quiet evenings curled up on the couch.',
                'personality': 'Gentle, calm, loves cuddles, enjoys sunbathing.',
            },
            {
                'name': 'Milo',
                'species': 'cat',
                'breed': 'Siamese',
                'age': '1.5 years',
                'gender': 'male',
                'description': 'Milo is a talkative Siamese with a playful streak. He greets everyone with a meow and loves interactive toys. He is social and thrives on companionship.',
                'personality': 'Vocal, playful, friendly, curious about everything.',
            },
            {
                'name': 'Whiskers',
                'species': 'cat',
                'breed': 'Tabby',
                'age': '3 years',
                'gender': 'male',
                'description': 'Whiskers is a classic tabby with gorgeous markings. He is independent yet affectionate on his own terms. He enjoys exploring and climbing to high perches.',
                'personality': 'Independent, adventurous, enjoys high places, loyal.',
            },
            {
                'name': 'Cleo',
                'species': 'cat',
                'breed': 'Maine Coon',
                'age': '4 years',
                'gender': 'female',
                'description': 'Cleo is a majestic Maine Coon with a luxurious coat. Despite her regal appearance, she is a gentle giant who loves belly rubs and playing with feather toys.',
                'personality': 'Gentle giant, playful, affectionate, loves water.',
            },
            {
                'name': 'Oliver',
                'species': 'cat',
                'breed': 'British Shorthair',
                'age': '2.5 years',
                'gender': 'male',
                'description': 'Oliver is a chubby British Shorthair with a teddy bear face. He is the definition of a lap cat — he will sit on your lap for hours purring contentedly.',
                'personality': 'Lazy, loves laps, purrs constantly, food enthusiast.',
            },
            {
                'name': 'Nala',
                'species': 'cat',
                'breed': 'Bengal',
                'age': '1 year',
                'gender': 'female',
                'description': 'Nala is a stunning Bengal kitten with wild markings. She is incredibly energetic and loves to play fetch. She needs an active family who can match her energy.',
                'personality': 'Energetic, loves fetch, intelligent, athletic.',
            },
        ]

        dogs = [
            {
                'name': 'Buddy',
                'species': 'dog',
                'breed': 'Golden Retriever',
                'age': '3 years',
                'gender': 'male',
                'description': 'Buddy is the quintessential family dog. This golden boy loves swimming, playing fetch, and greeting everyone with a wagging tail. He is well-trained and incredibly gentle with children.',
                'personality': 'Loyal, gentle, loves swimming, great with kids.',
            },
            {
                'name': 'Bella',
                'species': 'dog',
                'breed': 'Labrador',
                'age': '2 years',
                'gender': 'female',
                'description': 'Bella is a chocolate Labrador with endless energy and a heart of gold. She loves outdoor adventures, long walks, and will always be by your side. She is house-trained and knows basic commands.',
                'personality': 'Energetic, loving, adventurous, eager to please.',
            },
            {
                'name': 'Max',
                'species': 'dog',
                'breed': 'German Shepherd',
                'age': '4 years',
                'gender': 'male',
                'description': 'Max is a loyal and intelligent German Shepherd. He is protective of his family and incredibly trainable. He loves learning new tricks and enjoys agility exercises.',
                'personality': 'Intelligent, protective, trainable, alert.',
            },
            {
                'name': 'Daisy',
                'species': 'dog',
                'breed': 'Beagle',
                'age': '1.5 years',
                'gender': 'female',
                'description': 'Daisy is a curious Beagle with an extraordinary nose. She loves sniffing out treats and going on scent walks. Her adorable howl and floppy ears make everyone smile.',
                'personality': 'Curious, food-motivated, howls adorably, friendly.',
            },
            {
                'name': 'Rocky',
                'species': 'dog',
                'breed': 'Indie (Indian Pariah)',
                'age': '2 years',
                'gender': 'male',
                'description': 'Rocky is a resilient Indie dog rescued from the streets. He has adapted beautifully to home life and shows gratitude in everything he does. He is healthy, smart, and deeply loyal.',
                'personality': 'Resilient, grateful, smart, low-maintenance.',
            },
            {
                'name': 'Cookie',
                'species': 'dog',
                'breed': 'Pomeranian',
                'age': '1 year',
                'gender': 'female',
                'description': 'Cookie is a tiny Pomeranian with a big personality! She loves being the center of attention and enjoys being carried around. Despite her small size, she is fearless and full of energy.',
                'personality': 'Sassy, energetic, loves attention, fearless.',
            },
        ]

        all_pets = cats + dogs
        for pet_data in all_pets:
            Pet.objects.create(**pet_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(all_pets)} pets (6 cats, 6 dogs).'))
